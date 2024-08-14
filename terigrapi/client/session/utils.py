import datetime
import enum
import json
import urllib

from terigrapi.constants import UNSET


class InstagrapiJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, enum.Enum):
            return obj.value
        elif isinstance(obj, datetime.time):
            return obj.strftime("%H:%M")
        elif isinstance(obj, (datetime.datetime, datetime.date)):
            return int(obj.strftime("%s"))
        elif isinstance(obj, set):
            return list(obj)
        return json.JSONEncoder.default(self, obj)


def ig_dumps(data):
    """Json dumps format as required Instagram"""
    return InstagrapiJSONEncoder(separators=(",", ":")).encode(data)


def generate_signature(data):
    """Generate signature of POST data for Private API

    Returns
    -------
    str
        e.g. "signed_body=SIGNATURE.test"
    """
    return "signed_body=SIGNATURE.{data}".format(data=urllib.parse.quote_plus(data))


def clear_data(data, exclude: tuple = (UNSET,)):
    if isinstance(data, dict):
        return {k: clear_data(v) for k, v in data.items() if v not in exclude}
    if isinstance(data, list):
        return [clear_data(x) for x in data if x not in exclude]
    if isinstance(data, set):
        return {clear_data(x) for x in data if x not in exclude}
    return data
