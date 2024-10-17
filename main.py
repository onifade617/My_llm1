# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 09:14:32 2024

@author: Awarri User
"""

import streamlit as st
from langchain_community.llms import Ollama
import langchain

# Initialize the Ollama model (assuming 'llama3' is a valid model name)
llm = Ollama(model="llama3:7b")

# Streamlit header
st.header("Ask Ollama")

# Text input for user prompt
user_input = st.text_input("Ask a question:")

# Button to submit the question
if st.button("Submit"):
    if user_input:
        # Invoke the LLM with the user's question
        response = llm.invoke(user_input, stop=['<|eot_id|>'])
        
        # Display the response in Streamlit
        st.write(f"Response: {response}")
    else:
        st.write("Please enter a question.")