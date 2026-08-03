# 📰 TruthLens – AI Fake News and Misinformation Detection System

## Overview

TruthLens is an AI-powered Fake News Detection System that classifies news headlines as **Real** or **Fake** using Natural Language Processing (NLP) and Machine Learning. The project also provides explainable predictions using LIME and an interactive Streamlit web application.

---

## Features

- 📰 Fake News Detection
- 🔍 TF-IDF Feature Extraction
- 🤖 Linear SVM Classifier
- 🚀 Passive Aggressive Classifier
- 🧠 DistilBERT Model Comparison
- 💡 LIME Explainable AI
- 🌐 Streamlit Web Application
- 🗄️ SQLite Database for Prediction History
- 📊 Dataset Insights Dashboard

---

## Dataset

This project uses publicly available datasets:

- PolitiFact
- GossipCop

The processed dataset (`final_dataset.zip`) is included in compressed format. Extract it into the `dataset/` directory before running the project.

---

## Technologies Used

- Python
- Scikit-learn
- Streamlit
- SQLite
- Pandas
- NumPy
- Transformers
- DistilBERT
- LIME
- Matplotlib
- Seaborn

---

## Model Performance

| Model | Accuracy |
|--------|----------|
| Passive Aggressive | **80.00%** |
| Linear SVM | **84.07%** |
| DistilBERT | **85.93%** |

---

## Project Structure

```text
TruthLens-AI-Fake-News-Detection/
│
├── assets/
├── data_processing/
├── database/
├── dataset/
├── models/
├── notebooks/
├── pages/
├── streamlit/
├── styles/
│
├── app.py
├── requirements.txt
└── README.md
```

---

## Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Extract `final_dataset.zip` into the `dataset/` folder.

Run the Streamlit application:

```bash
streamlit run app.py
```

---

## DistilBERT Model

The fine-tuned DistilBERT model weights (`model.safetensors`) are **not included** in this repository because they exceed GitHub's maximum file size limit.

To reproduce the DistilBERT results:

1. Install the required dependencies.
2. Open the DistilBERT training notebook in the `notebooks/` directory.
3. Run all cells to train the model.
4. The trained model will be automatically saved in the `models/` directory.

---

## Future Improvements

- Real-time News API Integration
- Multi-language Fake News Detection
- Model Deployment on Cloud
- Enhanced Explainability Techniques

---

## Author

**Ayush Mittal**
