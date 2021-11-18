import logging
import itertools
from .google import scraper_google
from .apple import scraper_apple

__all__ = ["scraper", "scraper_google", "scraper_apple"]


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
            yield review

    for country in countries:
        logging.info(f"read reviews on {country} @ apple")
        for review in scraper_apple(apple_name, country, count):
            yield review
