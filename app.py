import os
from flask import Flask, render_template, request, Response
import openai
from dotenv import load_dotenv
import skydelsdx
from skydelsdx.commands import *
import datetime


load_dotenv() # loading .env file which contain the API key
openai.api_key = os.getenv("OPENAI_API_KEY")
app = Flask("Sky-GPT")  # Application name

sim = None
check_skydel_connection = False  # Global variable to track Skydel connection

@app.route("/") # Road toward a specific URL, here '/' represents the project home page
def home():     # Called function when the user access to the specified path
    return render_template('index.html') # Call HTML file to display


@app.route("/prompt", methods=["POST"])
def prompt():

    messages = request.json['messages']  # Recovering all the data in the 'messages' key created in the js file
    print(messages[-1])
    sendCommandToSkydel(messages[-1])

    return messages

# @app.route("/prompt", methods=["POST"])
# def prompt():   # Function to recover the text from the frontend
#
#     messages = request.json['messages'] # Recovering all the data in the 'messages' key created in the js file
#     conversation = FormatedConversationToSend(messages=messages) # send the messages to the function to format them for chat GPT API (list of dictionaries)
#     return Response(event_stream(conversation), mimetype = 'text/event-stream')

def createNewConfiguration():
    # Connect
    sim = skydelsdx.RemoteSimulator()
    sim.setVerbose(True)
    sim.connect()  # same as sim.connect("localhost")
    # Create new config
    sim.call(New(True))
    return sim

def sendCommandToSkydel(command):

    global sim  #Access the global sim object
    global check_skydel_connection

    if check_skydel_connection == False:  # Check if Skydel is connected
        sim = createNewConfiguration()  # Function call to set up a connection with a Skydel instance and initialization of a new config
        print("Skydel connection established")  # Response after connection
        check_skydel_connection = True  # Set the flag to 'True' after connecting

    if command == "sim.start()":
        sim.call(SetModulationTarget("NoneRT", "", "", True, "uniqueId"))
        sim.call(ChangeModulationTargetSignals(0, 12500000, 100000000, "UpperL", "L1CA", -1, False, "uniqueId")) # Minimum required configuration to start a simulation
        #sim.call(SetVehicleTrajectoryCircular("Circular", 0.7853995339022749, -1.2740964277717111, 0, 50, 3, True))
        #sim.call(SetGpsStartTime(datetime.datetime(2021, 2, 15, 7, 0, 0)))
        #sim.call(SetVehicleAntennaGain([], AntennaPatternType.AntennaNone, GNSSBand.L1))
        sim.arm()
        sim.start()
    elif command == "sim.stop()":
        sim.stop()

    # sim.call(SetModulationTarget(command))

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