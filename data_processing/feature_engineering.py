import pickle

from sklearn.feature_extraction.text import TfidfVectorizer


def create_tfidf_features(
    train_text,
    test_text=None,
    max_features=5000
):
    """
    Create TF-IDF features.
    """

    tfidf = TfidfVectorizer(
        max_features=max_features,
        ngram_range=(1, 2),
        stop_words='english'
    )

    X_train = tfidf.fit_transform(train_text)

    if test_text is not None:
        X_test = tfidf.transform(test_text)

        return X_train, X_test, tfidf

    return X_train, tfidf


def save_vectorizer(tfidf, path):
    """
    Save TF-IDF vectorizer.
    """

    with open(path, "wb") as file:
        pickle.dump(tfidf, file)


def load_vectorizer(path):
    """
    Load saved TF-IDF vectorizer.
    """

    with open(path, "rb") as file:
        return pickle.load(file)