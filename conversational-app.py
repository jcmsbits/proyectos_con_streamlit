from langchain_community.llms import LlamaCpp
import streamlit as st
import numpy as np
# with st.chat_message("user"):
#     st.write("Hello 👋")

# Define the model path
model_path = "./model/Model-1.2B-Q8_0.gguf"

llm = LlamaCpp(
    model_path=model_path,
    temperature=0.8,
    max_tokens=250,
    top_p=0.6,    
    verbose=True
)

# with st.chat_message("assistant"):
#     st.write("Hello human")
#     st.bar_chart(np.random.randn(30, 3))

prompt = st.chat_input("Say something")

if prompt:
    st.write(f"User has sent the following prompt: {prompt}")