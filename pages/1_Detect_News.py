import numpy as np
import streamlit as st
import pickle

from database.db_utils import save_prediction

# Load Model
svm_model = pickle.load(
    open("models/svm_model.pkl", "rb")
)

tfidf = pickle.load(
    open("models/tfidf.pkl", "rb")
)

st.title("📰 News Detection")

news = st.text_area(
    "Enter News Headline"
)

if st.button("Predict"):

    if news.strip() == "":
        st.warning(
            "Please enter a headline."
        )

    else:

        vector = tfidf.transform([news])

        prediction = svm_model.predict(vector)[0]

        # Get decision score
        decision_score = svm_model.decision_function(vector)[0]
        
        # Convert score into confidence %
        confidence = (
            1 / (1 + np.exp(-abs(decision_score)))
        ) * 100

        
        
        if prediction == 0:

            st.error("🚨 Fake News")
        
            save_prediction(
                news,
                "Fake News",
                round(confidence, 2)
            )
        
        else:
        
            st.success("✅ Real News")
        
            save_prediction(
                news,
                "Real News",
                round(confidence, 2)
            )
        
        st.metric(
            "Confidence",
            f"{confidence:.2f}%"
        )
        
        if confidence >= 90:
            st.success("🟢 Very High Confidence")
        elif confidence >= 75:
            st.info("🔵 High Confidence")
        elif confidence >= 60:
            st.warning("🟡 Moderate Confidence")
        else:
            st.error("🔴 Low Confidence")