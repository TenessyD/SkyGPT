import os
from flask import Flask, render_template
import openai
from dotenv import load_dotenv
import skydelsdx

load_dotenv() #loading .env file which contain the API key
openai.api_key = os.getenv("OPENAI_API_KEY")
app = Flask("Sky-GPT")  # Application name

@app.route("/")

def home():
    return render_template('index.html')

def buildConversationStructure(messages: list) -> list[dict]: # Creating a dictionnaire from the list of message as requested from Open AI API
    return [
        {"role": "user" if i%2 == 0 else "assistant", "content": message} # Checking thanks to the modulo operation whether the message comes from the user or chat GPT
         for i, message in enumerate(messages)
    ]

def even_stream(conversation:list[dict]) -> str:
    response = openai.chat.completion.create(
        model = "gpt-3.5-turbo",
        messages=conversation,
        stream=True
    )

if __name__=='__main__':
    #app.run(debug=True, host='127.0.0.1', port=5000) # Realized Flask server location
    print(buildConversationStructure(messages=["Bonjour, comment ca va ?","Ca va bien et toi ?", "Super merci!"]))

# 1:07:49