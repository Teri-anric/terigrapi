import time
import random
import asyncio
from uuid import uuid4

def generate_str_uuid():
    return str(uuid4())


def date_time_original(localtime):
    # return time.strftime("%Y:%m:%d+%H:%M:%S", localtime)
    return time.strftime("%Y%m%dT%H%M%S.000Z", localtime)


async def random_delay(delay_range: list):
    """Trigger sleep of a random floating number in range min_sleep to max_sleep"""
    return await asyncio.sleep(random.uniform(delay_range[0], delay_range[1]))
