#! /usr/bin/env python
#
#
# @file: common
# @time: 2021/11/18
# @author: Mori
#

import time
import logging
from functools import wraps

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s %(name)s %(levelname)s:%(message)s"
)


def logit(func):
    @wraps(func)
    def _wrapper_(*args, **kwargs):
        start = time.time()
        logging.info(f"starting job - {func.__name__}")
        result = func(*args, **kwargs)
        duration = time.time() - start
        logging.info(f"finish job - {func.__name__} in {round(duration, 3)} second")
        return result

    return _wrapper_
