import sys
from utils import logit
from scraper import scraper
from nlp import build_tfidf

from keybert import KeyBERT

args = sys.argv[1:]
apps = (args + [None, None])[:2]
google_package, apple_name = apps[0], apps[1]


@logit
def scrap():
    with open("documents", "w") as _f:
        for review_content in scraper(google_package, apple_name):
            _f.write(review_content.strip() + "\n")


@logit
def nlp():
    with open("documents", "r") as _rf, open("tfidf", "w") as _wf:
        content = _rf.readlines()
        for word in build_tfidf(content):
            _wf.write(word + "\n")


if __name__ == "__main__":
    scrap()
    # nlp()
    # keybert_model = KeyBERT()
    # with open("documents", "r") as _rf:
    #     content = _rf.readlines()
    #     keybert_model.extract_keywords(content, keyphrase_ngram_range=(1, 2))
