# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 09:14:32 2024

@author: Awarri User
"""

import streamlit as st
import langchain
from langchain_community.llms import ollama


llm = ollama(model = "llama3")

st.write(llm.invoke("Tell me the president of Nigeria", stop=['<|eot_id|>']))