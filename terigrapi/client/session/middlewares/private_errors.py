from typing import Any, Coroutine, TYPE_CHECKING

from terigrapi.client.exeptions import (BadPassword, ClientRequestTimeout, ClientForbiddenError, ClientNotFoundError, ClientStatusFail, InvalidMediaId, ChallengeRequired, CheckpointRequired, ClientError, ClientUnknownError, ConsentRequired, FeedbackRequired, GeoBlockRequired, InvalidTargetUser, LoginRequired, MediaUnavailable, PleaseWaitFewMinutes, PrivateAccount, ProxyAddressIsBlocked, RateLimitError, SentryBlock, TwoFactorRequired, UnknownError, UserNotFound, VideoTooLongException)

from pydantic import BaseModel

from terigrapi.client.session.middlewares.base import NextRequestMiddlewareType
from terigrapi.methods.base import InstagramMethod, InstagramType
from .base import BaseRequestMiddleware

if TYPE_CHECKING:
    from terigrapi.client.client import Client



class PrivateErrorHandler(BaseRequestMiddleware):
    def _get_result_value(self, result, key, default = None):
        value = getattr(result, key, default)
        if isinstance(result, dict):
            value = result.get(key, default)
        return value
            
    async def __call__(self, make_request: NextRequestMiddlewareType[InstagramType], client: "Client", method: InstagramMethod[InstagramType]) -> Coroutine[Any, Any, InstagramType]:
        try:
            result = await make_request(client, method)

            status = self._get_result_value(result, "status", "")
            if status == "fail":
                message = self._get_result_value(result, "message", "")
                raise ClientStatusFail(message, result=result)
            
            return result
        
        except (ClientNotFoundError, ClientRequestTimeout) as e:
            raise e from e # skip errors
        
        except ClientError as e:
            if e.response is None:
                raise e from e
            
            message = self._get_result_value(e.result, "message", "")
            error_type = self._get_result_value(e.result, "error_type", "")

            error_kwargs = dict(response=e.response, result=e.result)

            if "Please wait a few minutes" in message:
                raise PleaseWaitFewMinutes(e, **error_kwargs) from e

            match e.code:
                case 400:
                    if message == "challenge_required":
                        raise ChallengeRequired() from e
                    elif message == "feedback_required":
                        feedback_message = self._get_result_value(e.result, "feedback_message", "")
                        raise FeedbackRequired(f"{message}: {feedback_message}", **error_kwargs) from e
                    elif message == "consent_required":
                        raise ConsentRequired(**error_kwargs) from e
                    elif message == "geoblock_required":
                        raise GeoBlockRequired(**error_kwargs) from e
                    elif message == "checkpoint_required":
                        raise CheckpointRequired(**error_kwargs) from e
                    elif error_type == "sentry_block":
                        raise SentryBlock(**error_kwargs) from e
                    elif error_type == "rate_limit_error":
                        raise RateLimitError(**error_kwargs) from e
                    elif error_type == "bad_password":
                        raise BadPassword(**error_kwargs) from e
                    elif error_type == "two_factor_required":
                        raise TwoFactorRequired(message or "Two-factor authentication required", **error_kwargs) from e
                    elif "Please wait a few minutes before you try again" in message:
                        raise PleaseWaitFewMinutes(e, **error_kwargs) from e
                    elif "VideoTooLongException" in message:
                        raise VideoTooLongException(e, **error_kwargs) from e
                    elif "Not authorized to view user" in message:
                        raise PrivateAccount(e, **error_kwargs) from e
                    elif "Invalid target user" in message:
                        raise InvalidTargetUser(e, **error_kwargs) from e
                    elif "Invalid media_id" in message:
                        raise InvalidMediaId(e, **error_kwargs) from e
                    elif (
                        "Media is unavailable" in message
                        or "Media not found or unavailable" in message
                    ):
                        raise MediaUnavailable(e, **error_kwargs) from e
                    elif "has been deleted" in message:
                        # Sorry, this photo has been deleted.
                        raise MediaUnavailable(e, **error_kwargs) from e
                    elif (
                        "unable to fetch followers" in message
                        or "Error generating user info response" in message
                    ):
                        # returned when user not found
                        raise UserNotFound(e, **error_kwargs) from e
                    elif "The username you entered" in message:
                        # The username you entered doesn't appear to belong to an account.
                        # Please check your username and try again.
                        raise ProxyAddressIsBlocked(
                            "Instagram has blocked your IP address, "
                            "use a quality proxy provider (not free, not shared)"
                            **error_kwargs
                        ) from e
                    elif error_type or message:
                        raise UnknownError(**error_kwargs) from e
                    raise e from e # ClientBadRequestError
                case 403:
                    if message == "login_required":
                        raise LoginRequired(**error_kwargs) from e
                    if e.response and len(e.response.text) < 512:
                        message = e.response.text
                    raise ClientForbiddenError(e, message=message, **error_kwargs) from e
                case 429:
                    if "Please wait a few minutes before you try again" in message:
                        raise PleaseWaitFewMinutes(e, **error_kwargs) from e
                    raise e from e# ClientThrottledError 
                case _:
                    raise ClientUnknownError(e, **error_kwargs) from e


