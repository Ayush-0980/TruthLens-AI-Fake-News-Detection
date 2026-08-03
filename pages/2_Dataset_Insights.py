import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Dataset Insights")

df = pd.read_csv("dataset/final_dataset.csv")

fake_count = len(df[df["label"] == 0])
real_count = len(df[df["label"] == 1])

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Articles",
    len(df)
)

col2.metric(
    "Real News",
    real_count
)

col3.metric(
    "Fake News",
    fake_count
)

# Class Distribution

st.subheader("Fake vs Real Distribution")

counts = df["label"].map(
    {
        0:"Fake",
        1:"Real"
    }
).value_counts()

fig, ax = plt.subplots()

counts.plot(
    kind="bar",
    ax=ax
)

st.pyplot(fig)

# Headline Length

st.subheader(
    "Headline Length Distribution"
)

df["title_length"] = df["title"].astype(str).apply(len)

fig, ax = plt.subplots()

ax.hist(
    df["title_length"],
    bins=30
)

st.pyplot(fig)

# Word Count

st.subheader(
    "Word Count Distribution"
)

df["word_count"] = df["title"].astype(str).apply(
    lambda x: len(x.split())
)

fig, ax = plt.subplots()

ax.hist(
    df["word_count"],
    bins=20
)

st.pyplot(fig)

# Word Cloud

from wordcloud import WordCloud

st.subheader("☁️ Word Cloud")

text = " ".join(df["title"].astype(str))

wordcloud = WordCloud(
    width=800,
    height=400,
    background_color="white"
).generate(text)

fig, ax = plt.subplots(figsize=(10,5))

ax.imshow(
    wordcloud,
    interpolation="bilinear"
)

ax.axis("off")

st.pyplot(fig)

# Top 20 Most Common Words

from sklearn.feature_extraction.text import CountVectorizer

st.subheader("🔤 Top 20 Most Common Words")

vectorizer = CountVectorizer(
    stop_words="english"
)

X = vectorizer.fit_transform(
    df["title"]
)

word_counts = X.toarray().sum(axis=0)

words = vectorizer.get_feature_names_out()

word_freq = pd.DataFrame({
    "word": words,
    "count": word_counts
})

top_words = word_freq.sort_values(
    by="count",
    ascending=False
).head(20)

fig, ax = plt.subplots(
    figsize=(10,6)
)

ax.barh(
    top_words["word"],
    top_words["count"]
)

ax.set_xlabel("Frequency")

st.pyplot(fig)

# Fake vs Real Headline Comparison

st.subheader(
    "📦 Fake vs Real Headline Comparison"
)

fake_titles = df[
    df["label"] == 0
]["word_count"]

real_titles = df[
    df["label"] == 1
]["word_count"]

fig, ax = plt.subplots(
    figsize=(8,5)
)

ax.boxplot(
    [
        fake_titles,
        real_titles
    ],
    labels=[
        "Fake",
        "Real"
    ]
)

ax.set_ylabel(
    "Words per Headline"
)

st.pyplot(fig)