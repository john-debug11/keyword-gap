import streamlit as st
from google.cloud import aiplatform
import pandas as pd

# Function to analyze keywords
def analyze_keywords(primary_keyword, url, competitor_keywords):
    client = aiplatform.gapic.PredictionServiceClient()
    endpoint = "projects/YOUR_PROJECT_ID/locations/us-central1/endpoints/YOUR_ENDPOINT_ID"

    instance = {
        "system_instruction": "You are an SEO expert. Analyze the following primary keyword.",
        "prompt": f"Analyze the primary keyword: {primary_keyword} and provide suggestions.",
        "input": {
            "primary_keywords": primary_keyword,
            "url": url,
            "competitor_keywords": competitor_keywords
        }
    }
    response = client.predict(endpoint=endpoint, instances=[instance])
    return response.predictions

# Streamlit UI
st.title("SEO Keyword Analysis Tool")

with st.form("keyword_analysis_form"):
    primary_keyword = st.text_input("Enter Primary Keyword")
    url = st.text_input("Enter Website URL")
    competitor_keywords = st.text_area("Enter Competitor Keywords (comma separated)")

    submitted = st.form_submit_button("Analyze")
    if submitted:
        result = analyze_keywords(primary_keyword, url, competitor_keywords.split(","))
        st.subheader("Results")
        st.json(result)
