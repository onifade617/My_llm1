# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 09:14:32 2024

@author: Awarri User
"""

import streamlit as st
from transformers import AutoTokenizer,AutoModelForCausalLM
from transformers import pipeline
import transformers
import torch


model_name = "meta-llama/Llama-2-7b-hf"

tokenizer = AutoTokenizer.from_pretrained(model_name, token = "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")

model = AutoModelForCausalLM.from_pretrained(model_name, token = "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")


# Set up the Streamlit app
st.title("LLaMA Chatbot")
st.write("Talk to LLaMA!")
