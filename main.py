# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 09:14:32 2024

@author: Awarri User
"""

import streamlit as st
from transformers import pipeline

# Initialize the text-generation pipeline with the Llama-2 model
pipe = pipeline("text-generation", model="meta-llama/Llama-2-70b-chat-hf")

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
