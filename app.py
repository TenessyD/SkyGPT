import os
from flask import Flask, render_template, request, Response
import openai
from dotenv import load_dotenv
from skydel_manager import SkydelManager

load_dotenv() # Loading .env file which contain the API key
openai.api_key = os.getenv("OPENAI_API_KEY")
app = Flask("Sky-GPT")  # Application name

skydel_manager = SkydelManager() # Initializing Skydel manager

@app.route("/") # Road toward a specific URL, here '/' represents the project home page
def home():     # Called function when the user access to the specified path
    return render_template('index.html') # Call HTML file to display

@app.route("/prompt", methods=["POST"])
def prompt():
    messages = request.json['messages']  # Recovering all the data in the 'messages' key created in the js file
    print(messages[-1])
    skydel_manager.sendCommand(messages[-1])
    return messages

# @app.route("/prompt", methods=["POST"])
# def prompt():   # Function to recover the text from the frontend
#
#     messages = request.json['messages'] # Recovering all the data in the 'messages' key created in the js file
#     conversation = FormatedConversationToSend(messages=messages) # send the messages to the function to format them for chat GPT API (list of dictionaries)
#     return Response(event_stream(conversation), mimetype = 'text/event-stream')

def event_stream(conversation:list[dict]) -> str:
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = conversation,
        stream = True  # Enable the response to be display part by part
    )

    for line in response:
        text = line.choices[0].delta.get('content','') # Get message content from the response
        if len(text):
            yield text  # generator to display the message by parts

def FormatedConversationToSend(messages: list) -> list[dict]: # Creating a list of dictionary formated as requested by Open AI API doc
    return [
        {"role": "user" if i%2 == 0 else "assistant", "content": message} # Checking thanks to the modulo operation whether the message comes from the user or chat GPT
         for i, message in enumerate(messages)
    ]
if __name__=='__main__':  # Execution of the code behind the condition
    app.run(debug=True, host='127.0.0.1', port=5000) # Launching the web server on the specified location (127.0.0.1 = locally hosted)




# 1:07:49