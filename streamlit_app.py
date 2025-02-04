import os
import streamlit as st
import google.generativeai as genai

# Load environment variables from .env file


# Configure Gemini API
API_KEY ="AIzaSyDNMGZL6x1Qn_4PQ6QlK0pqhFg1wP0kdEU"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

# Function to interact with Gemini API
def chat_with_gemini(message):
    response = model.generate_content(message)
    return response.text  # Returns the generated text

# Streamlit Page Configuration
st.set_page_config(page_title="MSTravel Chatbot", page_icon="Ⓜ️", layout="wide")

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
    st.session_state.chat_history.append({"role": "assistant", "content": "Hi, I am MSTravel Bot! How can I assist you with tourism-related questions?"})

# Display Chat History
st.markdown("### MSTravel Chatbot")
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat Input Box (Fixed at Bottom)
user_input = st.chat_input("Ask about tourism, destinations, or trip planning...")
if user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    # Send the message directly to Gemini with a tourism-specific instruction
    prompt = f"You are a professional and friendly tourism assistant. You specialize in answering travel-related questions and providing helpful information about tourism in various countries. Please provide a concise, clear answer to the following question: {user_input}. Additionally, after answering, kindly ask any relevant questions about the user's travel preferences or plans. At the end of the conversation, create a summarized travel plan with helpful icons/emojis."

    response_text = chat_with_gemini(prompt)

    st.session_state.chat_history.append({"role": "assistant", "content": response_text})
    st.rerun()
