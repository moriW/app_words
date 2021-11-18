#! /usr/bin/env python
# 
#
# @file: apple
# @time: 2021/11/17
# @author: Mori
#

from typing import Iterator
from app_store_scraper import AppStore

def scraper_apple(app: str, country: str, count: int) -> Iterator[str]:
    app_store = AppStore(app_name=app, country=country)
    app_store.review(how_many=count, sleep=1)
    for review in app_store.reviews:
        yield f"{review['title']}. {review['review']}"