import streamlit as st

st.set_page_config(
    page_title="TruthLens",
    page_icon="📰",
    layout="wide"
)

st.title("📰 TruthLens")
st.markdown("""
### 🛡️ Detect Misinformation Using Artificial Intelligence

TruthLens leverages Machine Learning and Explainable AI to
classify news headlines as **Real** or **Fake**, helping users
identify misinformation quickly and transparently.
""")
st.subheader(
    "AI Powered Fake News Detection System"
)

st.markdown("---")
st.info("""
🛡️ TruthLens uses Machine Learning and Explainable AI
to classify news headlines as Real or Fake.

Datasets Used:
• PolitiFact
• GossipCop

Best Model:
• Linear SVM (84.07% Accuracy)
""")
# Metrics

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "News Articles",
    "23,196"
)

col2.metric(
    "Accuracy",
    "84.07%"
)

col3.metric(
    "ML Models",
    "2"
)

col4.metric(
    "Explainable AI",
    "Enabled"
)

st.markdown("---")

st.header("🎯 Project Objective")

st.markdown("---")

st.header("🔄 System Architecture")

st.image(
    "assets/workflow.png",
    use_container_width=True
)

st.write(
    """
    TruthLens is an AI-powered fake news detection
    system that analyzes news headlines and
    classifies them as Fake or Real using
    Machine Learning techniques.
    """
)

st.markdown("---")

st.header("🚀 Features")

st.markdown(
    """
    ✅ Fake News Detection

    ✅ Explainable AI (LIME)

    ✅ SQLite Prediction History

    ✅ Dataset Analytics Dashboard

    ✅ Confidence Score

    ✅ Multi-Page Streamlit Application
    """
)
st.markdown("---")
st.header("🛠 Technology Stack")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.info("🐍 Python")

with c2:
    st.info("🤖 Scikit-Learn")

with c3:
    st.info("🌐 Streamlit")

with c4:
    st.info("🗄 SQLite")



st.markdown("---")

st.header("📈 Dataset Summary")

st.write("""
• Total Articles: 23,196

• Real News: 17,441

• Fake News: 5,755

• Dataset Sources: PolitiFact & GossipCop
""")

st.markdown("---")
