# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 09:14:32 2024

@author: Awarri User
"""

import streamlit as st
from huggingface_hub import InferenceClient

# Initialize Hugging Face Inference Client with your API token
client = InferenceClient(api_key="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")  # Replace with your actual Hugging Face API key

# Streamlit header
st.header("Ask Hugging Face Llama-2 Model")

# Text input for user prompt
user_input = st.text_input("Ask a question:")

# Button to submit the question
if st.button("Submit"):
    if user_input:
        # Placeholder for the response to stream the content dynamically
        response_placeholder = st.empty()
        
        # Send the user's question to the Llama-2 model and stream the response
        try:
            response_text = ""
            for message in client.chat_completion(
                model="meta-llama/Llama-2-7b-chat-hf",  # Model to use
                messages=[{"role": "user", "content": user_input}],
                max_tokens=500,
                stream=True,
            ):
                # Stream the response to the placeholder dynamically
                content = message.choices[0].delta.get("content", "")
                response_text += content
                response_placeholder.text(response_text)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.write("Please enter a question.")
