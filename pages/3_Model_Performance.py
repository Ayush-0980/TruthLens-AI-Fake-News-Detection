import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("🤖 Model Performance")

comparison = pd.DataFrame({
    "Model":[
        "Linear SVM",
        "Passive Aggressive"
    ],
    "Accuracy":[
        0.840733,
        0.801940
    ]
})

st.dataframe(comparison)

fig, ax = plt.subplots()

ax.bar(
    comparison["Model"],
    comparison["Accuracy"]
)

ax.set_ylabel("Accuracy")

st.pyplot(fig)

st.success(
    "Linear SVM selected as final model."
)