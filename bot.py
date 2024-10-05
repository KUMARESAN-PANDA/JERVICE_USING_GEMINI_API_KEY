import os
import google.generativeai as genai
import streamlit as st
import time
from textblob import TextBlob  # For sentiment analysis

# Initialize the AI API
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# Create the model configuration
generation_config = {
    "temperature": 0,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Initialize the model with specified configuration
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

# Initialize chat history in Streamlit session state
if 'history' not in st.session_state:
    st.session_state.history = []

# Function to split text and code from response
def split_response(response_text):
    lines = response_text.split('\n')
    text_part = []
    code_part = []
    is_code = False
    
    for line in lines:
        if "```" in line:  # Detect start/end of code block
            is_code = not is_code
            continue
        if is_code:
            code_part.append(line)
        else:
            text_part.append(line)

    return '\n'.join(text_part), '\n'.join(code_part)

# Function to handle user input and get chatbot response
def get_chatbot_response(user_input):
    chat_session = model.start_chat()
    
    # Append user input to chat history
    st.session_state.history.append({"role": "user", "parts": [user_input]})
    
    # Send user message to model and retrieve response
    with st.spinner('Chatbot is thinking...'):
        response = chat_session.send_message(user_input)
    
    st.session_state.history.append({"role": "model", "parts": [response.text]})
    
    return response.text

# Function to display text with typing animation
def typing_animation(text, delay=0.01):
    message_placeholder = st.empty()  # Create a placeholder for dynamic updates
    displayed_text = ""
    
    for char in text:
        displayed_text += char
        message_placeholder.text(displayed_text)  # Update the placeholder with new content
        time.sleep(delay)  # Small delay to simulate typing

# Function for sentiment analysis
def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity
    if sentiment_score > 0:
        return "😊 Positive"
    elif sentiment_score < 0:
        return "😠 Negative"
    else:
        return "😐 Neutral"

# Function to clear chat history
def clear_chat():
    st.session_state.history = []

# Streamlit app layout
st.title("project jervice")

# Input box for user messages
user_input = st.text_input("You: ", "")

# Display sentiment analysis
if user_input:
    sentiment = analyze_sentiment(user_input)
    st.write(f"Sentiment: {sentiment}")

if user_input:
    if user_input.lower() == "exit":
        st.write("Ending chat session. Goodbye!")
        st.stop()
    else:
        response = get_chatbot_response(user_input)
        
        # Split response into text and code
        text, code = split_response(response)
        
        # Typing animation for text
        if text:
            typing_animation(text)
        
        # Display code if present
        if code:
            st.code(code, language='python')  # You can adjust the language as needed

# Display chat history
if st.checkbox("Show Chat History"):
    for entry in st.session_state.history:
        role = "You" if entry["role"] == "user" else "Chatbot"
        st.write(f"{role}: {' '.join(entry['parts'])}")

# Clear chat button
if st.button("Clear Chat"):
    clear_chat()
    st.experimental_rerun()
