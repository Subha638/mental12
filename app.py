import streamlit as st
from transformers import pipeline

# Initialize the Hugging Face model
@st.cache_resource
def load_model():
    return pipeline("text-generation", model="microsoft/DialoGPT-small")

chatbot = load_model()

# Sidebar navigation
page = st.sidebar.radio("📌 Navigate", ["Home", "Chat with AI", "Resources", "Emergency Help", "About"])

if page == "Home":
    st.title("🌱 Youth Mental Wellness")
    st.write("A safe, confidential space for young minds 💙")

elif page == "Chat with AI":
    st.title("🗨️ Confidential AI Chat")
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    user_input = st.chat_input("Type your message here...")

    if user_input:
        st.chat_message("user").write(user_input)
        st.session_state.messages.append({"role": "user", "content": user_input})

        ai_reply = chatbot(user_input, max_new_tokens=100, pad_token_id=50256)[0]["generated_text"]
        ai_reply = ai_reply[len(user_input):].strip()

        st.chat_message("assistant").write(ai_reply)
        st.session_state.messages.append({"role": "assistant", "content": ai_reply})

elif page == "Resources":
    st.title("📚 Resources for Mental Wellness")
    st.markdown("""
    - [Headspace](https://www.headspace.com/)
    - [NAMI](https://www.nami.org/Home)
    - [WHO Mental Health](https://www.who.int/health-topics/mental-health)
    - [TED Talks on Mental Health](https://www.ted.com/topics/mental+health)
    """)

elif page == "Emergency Help":
    st.title("🚨 Emergency Help")
    st.markdown("""
    - **US:** 988
    - **India:** +91-9582208181 (Snehi Helpline)
    - **UK:** 116 123 (Samaritans)
    """)

elif page == "About":
    st.title("ℹ️ About")
    st.write("This is an AI-powered youth mental wellness app built with Hugging Face models.")
