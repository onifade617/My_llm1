# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 09:14:32 2024

@author: Awarri User
"""

import streamlit as st
from transformers import pipeline
from huggingface_hub import login

# Hugging Face API Token (make sure to use your actual token)
hf_token = "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"

# Log in to Hugging Face using the token
login(token=hf_token)

# Initialize the text-generation pipeline with authenticated access
pipe = pipeline("text-generation", model="meta-llama/Llama-2-7b-chat-hf", device="cpu")

# Streamlit header
st.header("Ask the Llama-2 Model")

# Text input for user prompt
user_input = st.text_input("Ask a question:")

# Button to submit the question
if st.button("Submit"):
    if user_input:
        # Prepare the message in the format expected by the model
        messages = [{"role": "user", "content": user_input}]
        
        # Generate the response using the pipeline
        response = pipe(messages)
        
        # Display the response in Streamlit
        st.write(f"Response: {response[0]['generated_text']}")
    else:
        st.write("Please enter a question.")
