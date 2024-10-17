# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 09:14:32 2024

@author: Awarri User
"""

import streamlit as st
import requests

# Hugging Face API URL and model
API_URL = "https://api-inference.huggingface.co/models/meta-llama/Llama-2-7b-chat-hf"
API_TOKEN = "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"

# Function to query the Hugging Face API
def query_huggingface_api(prompt):
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    payload = {"inputs": prompt}
    
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

# Streamlit header
st.header("Ask a Question to Hugging Face Model")

# Text input for user prompt
user_input = st.text_input("Ask a question:")

# Button to submit the question
if st.button("Submit"):
    if user_input:
        # Query the Hugging Face model
        response = query_huggingface_api(user_input)
        
        # Display the response in Streamlit
        if "error" in response:
            st.error(f"Error: {response['error']}")
        else:
            st.write(f"Response: {response}")
    else:
        st.write("Please enter a question.")
