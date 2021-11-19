import os
import sys
import pickle

from utils import logit
from scraper import scraper
from nlp import build_tfidf


import nltk
from keybert import KeyBERT

args = sys.argv[1:]
apps = (args + [None, None])[:2]
google_package, apple_name = apps[0], apps[1]


DOCUMENTS_FOLDER = "documents"
KEYWORDS_FOLDER = "keywords"


for folder in [DOCUMENTS_FOLDER, KEYWORDS_FOLDER]:
    if not os.path.exists(folder):
        os.mkdir(folder)

document_path = os.path.join(DOCUMENTS_FOLDER, apple_name)
keyword_path = os.path.join(KEYWORDS_FOLDER, apple_name)


@logit
def scrap():
    if os.path.exists(document_path):
        return
    with open(document_path, "w") as _f:
        for review_content in scraper(google_package, apple_name, count=1000):
            _f.write(review_content.lower().strip() + "\n")


@logit
def nlp1():
    ps = nltk.PorterStemmer()
    keybert_model = KeyBERT()
    value_dict = {}
    with open(document_path, "r") as _f:
        content = _f.readlines()
        for raw_content, keyword_value_pair in zip(
            content, keybert_model.extract_keywords(content, top_n=100)
        ):
            keyword = [x[0] for x in keyword_value_pair]
            stem_tag = {
                ps.stem(word): tag
                for word, tag in nltk.pos_tag(nltk.tokenize.word_tokenize(raw_content))
                if word in keyword
            }

            for keyword, value in keyword_value_pair:
                stem = ps.stem(keyword)
                key = f"{stem} {stem_tag.get(stem, None)}"
                value_dict[key] = value_dict.get(key, {"count": 0, "value": 0})
                value_dict[key]["count"] += 1
                value_dict[key]["value"] += value

    with open(keyword_path, "wb") as _f:
        pickle.dump(value_dict, _f)


if __name__ == "__main__":
    scrap()
    nlp1()
