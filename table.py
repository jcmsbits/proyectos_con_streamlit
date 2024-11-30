import streamlit as st
import pandas as pd
import numpy as np


df = pd.DataFrame(
    np.random.randn(10, 10), columns=("col %d" % i for i in range(10))
)

st.markdown(
    """
    <style>
        section[data-testid="stSidebar"] {
            width: 100px !important; # Set the width to your desired value
        }
    </style>
    """,
    unsafe_allow_html=True,
)
st.markdown(
    """
    <style>
        section["data-testid="column""]:nth-of-type(2) {
            width: 25px !important; # Set the width to your desired value
            right: 0px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

col1, col2 = st.columns([0.5,0.5],vertical_alignment="center", gap ="large")

with st.sidebar:
    st.title('🤗💬 HugChat')

st.markdown(
    """
    <style>
       
        div[data-testid="container"]
        {
            border:1px solid blue;
            text-align: right;        
            right: 0px !important;
                
        } 
    </style>
    """,unsafe_allow_html=True
)


st.dataframe(df)

with col2:
    #with st.container(border=True, key="col2"):
    messages = st.container(height=300, border=True)
    if prompt := st.chat_input("Say something"):
        messages.chat_message("user").write(prompt)
        messages.chat_message("assistant").write(f"Echo: {prompt}")
