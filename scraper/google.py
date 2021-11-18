#! /usr/bin/env python
#
#
# @file: scraper
# @time: 2021/11/17
# @author: Mori
#

import logging
from typing import Iterable
from google_play_scraper import reviews


def scraper_google(
    app_name: str, lan: str = "en", country: str = "us", count: int = 10000
) -> Iterable[str]:
    continuation_token, _count, offset = None, 0, int(count / 10)

    while True:
        logging.info(f"loading from google {lan}, {country}, {_count}...")
        _result, continuation_token = reviews(
            app_name,
            count=offset,
            continuation_token=continuation_token,
            lang=lan,
            country=country,
        )

        for review in _result:
            yield review["content"]

        _count += len(_result)

        if continuation_token is None:
            break

        if _count >= count:
            break
