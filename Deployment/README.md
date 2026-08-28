# Deployment

This folder contains the Streamlit application used to deploy the Online Course Recommendation System.

## Application

`app.py`

The application allows users to select a course and receive the top 5 similar course recommendations.

## Recommendation Technique

- Content-Based Filtering
- TF-IDF Vectorization
- Cosine Similarity

## Run Locally

```bash
pip install -r requirements.txt
streamlit run Deployment/app.py
