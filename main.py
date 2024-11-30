import streamlit as st
st.set_page_config(page_title="🤗💬 HugChat")

st.title('🎈 App Name')

st.write('Hello world!')

with st.sidebar:
    st.title('🤗💬 HugChat')
    # if ('EMAIL' in st.secrets) and ('PASS' in st.secrets):
    #     st.success('HuggingFace Login credentials already provided!', icon='✅')
    #     hf_email = st.secrets['EMAIL']
    #     hf_pass = st.secrets['PASS']
    # else:
    # hf_email = st.text_input('Enter E-mail:', type='password')
    # hf_pass = st.text_input('Enter password:', type='password')
    # print(type(hf_email))
    # if not (hf_email and hf_pass):
    #     st.warning('Please enter your credentials!', icon='⚠️')
    # else:
    #     st.success('Proceed to entering your prompt message!', icon='👉')
    # st.markdown('📖 Learn how to build this app in this [blog](https://blog.streamlit.io/how-to-build-an-llm-powered-chatbot-with-streamlit/)!')

col1, col2 = st.columns([0.7,0.3])
with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")   

# Store LLM generated responses
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "How may I help you?"}]

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Function for generating LLM response
def generate_response(prompt_input, email, passwd):
    # Hugging Face Login
    sign = Login(email, passwd)
    cookies = sign.login()
    # Create ChatBot                        
    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
    return chatbot.chat(prompt_input)

# User-provided prompt
if prompt := st.chat_input(disabled=not (hf_email and hf_pass)):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)