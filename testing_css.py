import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(layout='wide')
df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))
# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []


# st.markdown(
#     """
#     <style>
#         div[data-testid="column"]:nth-of-type(1)
#         {
#             border:1px solid red;
#         } 

#         div[data-testid="column"]:nth-of-type(2)
#         {
#             border:1px solid blue;
#             text-align: end;
#         }
#          div[data-testid="column"]
#         {
#             position:absolute;
#             border:1px solid blue;
#             text-align: end;
#             right: 0px;
#         } 
#     </style>
#     """,unsafe_allow_html=True
# )
col1, col2 = st.columns([1,1,], gap="large")
st.markdown(
    """
    <style>
        div[data-testid="stVerticalBlockBorderWrapper"]
        {
            
            position:absolute;           
            text-align: end;
            right: 5px;
            width: 400px;
        } 
        
         
    </style>
    """,unsafe_allow_html=True
)
with st.sidebar:
    st.slider("Number")

with col1:
    st.dataframe(df)

with col2:
    with st.container(height=500,border=True, key="chat"):
            # Display chat messages from history on app rerun
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
                
            # Accept user input
        if prompt := st.chat_input("What is up?"):
            # Display user message in chat message container
            with st.chat_message("user"):
                st.markdown(prompt)
            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": prompt})

# col1, col2, col3 = st.columns(3)

# with col1:
#     """
#     ## Column 1 
#     Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
#     sed do eiusmod tempor incididunt ut labore et dolore 
#     magna aliqua. Volutpat sed cras ornare arcu dui vivamus.
#     """
# with col2:
#     """
#     ## Column 2
#     Stuff aligned to the right
#     """
#     st.button("➡️")


# with col3:
#     """
#     ## Column 3
#     This column was untouched by our CSS 
#     """
#     st.button("🐈")