GEMINI_API_KEY = "api-key" # Replace with your actual API key

import streamlit as st
import google.generativeai as genai




if not GEMINI_API_KEY:
    st.error("API key is missing. Please set the GEMINI_API_KEY in chatbot,py.")
    st.stop()

# Ensure Gemini API is configured
genai.configure(api_key=GEMINI_API_KEY)  

# Load Gemini model
model = genai.GenerativeModel("gemini-1.5-pro")

# Streamlit UI
st.title("🩺 Healthcare Triage Chatbot")
st.write("Describe your symptoms, and I'll suggest the right specialist.")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input field
user_input = st.chat_input("Describe your symptoms...")

if user_input:
    # Store user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate AI response
    with st.spinner("Analyzing symptoms..."):
        response = model.generate_content(f"Which medical specialist should I visit for these symptoms: {user_input}?")
        bot_reply = response.text.strip()

    with st.chat_message("assistant"):
        st.markdown(bot_reply)

    # Store AI response
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})