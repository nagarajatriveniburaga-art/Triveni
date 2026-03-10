import streamlit as st
import os
from groq import Groq
from dotenv import load_dotenv
# Load environment variables
load_dotenv()


client = Groq(api_key=os.getenv("Groq"))





# Title
st.title("🤖 AI Chat Assistant")





# Initialize session state
if "chat" not in st.session_state:
    st.session_state.chat = []


# Display chat history
for msg in st.session_state.chat:
    st.chat_message(msg["role"]).write(msg["content"])


# Chat input
prompt = st.chat_input("Type your message...")


if prompt:


    # Add user message
    st.session_state.chat.append({
        "role": "user",
        "content": prompt
    })




            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=st.session_state.chat
            )


            reply = response.choices[0].message.content


            


    # Save assistant reply
    st.session_state.chat.append({
        "role": "assistant",
        "content": reply
    })




