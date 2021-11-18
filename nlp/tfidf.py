from sklearn.feature_extraction.text import TfidfVectorizer, ENGLISH_STOP_WORDS


def build_tfidf(texts: list[str]):
    vectorizer = TfidfVectorizer(max_df=0.5)
    vectorizer.fit_transform(texts)

    for word in vectorizer.get_feature_names_out():
        if word not in ENGLISH_STOP_WORDS:
            yield word