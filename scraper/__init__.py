import logging
import itertools
from typing import Optional

import demoji

from .apple import scraper_apple
from .google import scraper_google

__all__ = ["scraper", "scraper_google", "scraper_apple"]


def content_filter(content: str) -> Optional[str]:
    content = demoji.replace(content)
    if len(content) < 20:
        return None
    content = " ".join(filter(lambda x: len(x) < 15, content.split()))
    return content


def scraper(
    google_package: str,
    apple_name: str,
    lans: list[str] = ["en"],
    countries: list[str] = ["us"],
    count: int = 10000,
):
    for lan, country in itertools.product(lans, countries):
        logging.info(f"read reviews on {lan}, {country} @ google")
        for review in scraper_google(google_package, lan, country, count):
            review = content_filter(review)
            if review: yield review

    for country in countries:
        logging.info(f"read reviews on {country} @ apple")
        for review in scraper_apple(apple_name, country, count):
            review = content_filter(review)
            if review: yield review
