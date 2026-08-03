import streamlit as st


st.title("ℹ️ About TruthLens")

st.markdown("---")

st.header("🎯 Project Overview")

st.write("""
TruthLens is an AI-powered Fake News Detection System designed to identify whether
a news headline is Real or Fake using Machine Learning techniques.

The system utilizes TF-IDF Vectorization and Linear SVM classification to analyze
news headlines and provide predictions along with confidence scores and explainable AI insights.
""")

st.markdown("---")

st.header("📚 Dataset Information")

st.markdown("""
### Data Sources

- **PolitiFact**
  - Political news fact-checking dataset
  - Contains real and fake political news

- **GossipCop**
  - Entertainment and celebrity news dataset
  - Contains verified real and fake news headlines

### Dataset Statistics

- Total Articles: **23,196**
- Real News: **17,441**
- Fake News: **5,755**
""")

st.markdown("---")

st.header("🛠 Technology Stack")

st.markdown("""
### Programming Language
- Python

### Machine Learning
- Scikit-Learn
- TF-IDF Vectorizer
- Linear SVM
- Passive Aggressive Classifier

### Explainable AI
- LIME (Local Interpretable Model-Agnostic Explanations)

### Database
- SQLite

### Web Framework
- Streamlit

### Data Analysis
- Pandas
- NumPy
- Matplotlib
- WordCloud
""")

st.markdown("---")

st.header("🚀 Key Features")

st.markdown("""
✅ Fake News Detection

✅ Explainable AI using LIME

✅ Confidence Score Prediction

✅ Dataset Analytics Dashboard

✅ Prediction History

✅ SQLite Database Storage

✅ Model Performance Comparison

✅ Streamlit Multi-Page Application
""")

st.markdown("---")

st.header("📈 Future Scope")

st.markdown("""
- Integration of Transformer Models (BERT, RoBERTa, DeBERTa)
- Real-time News Verification
- News URL Analysis
- Social Media News Detection
- User Authentication System
- Cloud Deployment
- API Integration
""")

st.markdown("---")

