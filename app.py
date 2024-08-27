import streamlit as st
from groq import Groq

st.title("Radha Chatbot Clone")
st.markdown(" Hi there! I am your assistant. How can I help you today?")
st.write("")

# Directly set your Groq API key
api_key = "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"

# Initialize Groq client with the API key
client = Groq(api_key=api_key)

# Set a default model
if "groq_model" not in st.session_state:
    st.session_state["groq_model"] = "llama3-8b-8192"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("heyy! Write Something Here.....?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Call Groq API and get assistant response
    with st.chat_message("assistant"):
        response = ""
        try:
            # Make the API call to generate the assistant's response
            chat_completion = client.chat.completions.create(
                model=st.session_state["groq_model"],
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ]
            )
            response = chat_completion.choices[0].message.content
            st.markdown(response)
        except Exception as e:
            st.error(f"An error occurred: {e}")

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
