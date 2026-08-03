import streamlit as st
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from lime.lime_text import LimeTextExplainer

# Load Model
svm_model = pickle.load(
    open("models/svm_model.pkl", "rb")
)

tfidf = pickle.load(
    open("models/tfidf.pkl", "rb")
)

st.title("🔍 Explain Prediction")

news = st.text_area(
    "Enter News Headline"
)

# Probability Function for LIME
def predict_proba(texts):

    vectors = tfidf.transform(texts)

    scores = svm_model.decision_function(vectors)

    probs = 1 / (1 + np.exp(-scores))

    return np.vstack(
        [1 - probs, probs]
    ).T


if st.button("Explain"):

    if news.strip() == "":

        st.warning(
            "Please enter a headline."
        )

    else:
        # Prediction
        vector = tfidf.transform([news])

        prediction = svm_model.predict(vector)[0]

        decision_score = svm_model.decision_function(vector)[0]

        confidence = (
            1 / (1 + np.exp(-abs(decision_score)))
        ) * 100

        # Display Prediction
        if prediction == 0:

            st.error("🚨 Fake News")

        else:

            st.success("✅ Real News")

        st.metric(
            "Confidence",
            f"{confidence:.2f}%"
        )
        
         # LIME Starts Here
        
        explainer = LimeTextExplainer(
            class_names=[
                "Fake News",
                "Real News"
            ]
        )

        exp = explainer.explain_instance(
            news,
            predict_proba,
            num_features=10
        )

        st.subheader(
            "Important Words"
        )

        explanation = exp.as_list()

        exp_df = pd.DataFrame(
            explanation,
            columns=[
                "Word",
                "Impact"
            ]
        )
        
        st.dataframe(
            exp_df,
            use_container_width=True,
            hide_index=True
        )

        # Word Importance Chart
        fig, ax = plt.subplots(
            figsize=(8,4)
        )
        
        ax.barh(
            exp_df["Word"],
            exp_df["Impact"]
        )
        
        ax.set_title(
            "Word Importance"
        )
        
        st.pyplot(fig)
        
        