# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 09:14:32 2024

@author: Awarri User
"""

import streamlit as st

from huggingface_hub import InferenceClient

client = InferenceClient(api_key="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")

for message in client.chat_completion(
	model="meta-llama/Llama-2-7b-chat-hf",
	messages=[{"role": "user", "content": "What is the capital of France?"}],
	max_tokens=500,
	stream=True,
):
    st.write(message.choices[0].delta.content, end="")