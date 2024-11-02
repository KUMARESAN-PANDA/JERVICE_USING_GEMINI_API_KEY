
# Project Jervice

## Overview

Project Jervice is a chatbot application built using Streamlit and Google Generative AI. It utilizes sentiment analysis to understand user inputs and provides responses accordingly. The application is designed to simulate a conversational experience and includes features such as typing animations and the ability to display code snippets.

## Features

- Chatbot powered by Google Generative AI.
- Sentiment analysis using TextBlob to gauge user emotions.
- Typing animation for a more interactive experience.
- Option to view chat history.
- Ability to clear chat history.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7 or higher
- Streamlit
- Google Generative AI package (`google.generativeai`)
- TextBlob

You will also need an API key for the Google Generative AI service.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com//KUMARESAN-PANDA/JERVICE_USING_GEMINI_API_KEY.git
   cd project-JERVICE_USING_GEMINI_API_KEY
   ```

2. Install the required packages:

   ```bash
   pip install streamlit google-generativeai textblob
   ```

3. Set up your environment variable for the API key:

   On Unix or MacOS, you can set the environment variable in your terminal:

   ```bash
   export GEMINI_API_KEY='your_api_key_here'
   ```

   On Windows, use:

   ```bash
   set GEMINI_API_KEY='your_api_key_here'
   ```

## Usage

To run the application, use the following command:

```bash
streamlit run app.py
```

Once the application is running, you can access it in your web browser at `http://localhost:8501`.

## Interaction

- Type your message in the input box and press Enter.
- The application will display the sentiment of your message.
- The chatbot's response will appear with a typing animation.
- You can view the chat history by checking the corresponding box.
- Press the "Clear Chat" button to reset the chat history.

