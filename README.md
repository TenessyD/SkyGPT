## Project Objectives
This project aims to develop an application that interfaces OpenAI's ChatGPT with Skydel to generate and run simulations
automatically, based on the user’s prompt-defined requirements. This application will help any Skydel user 
to easily create various testing scenarios to evaluate the performance of a GNSS receiver under different conditions.

## Technical details
Sky-GPT integrates ChatGPT through its Python API to automate the simulation configuration and execution on Skydel across its remote API.  
To run the app on your machine, you'll need to install `Flask`, the framework used to manage the python backend and `Tailwind CSS` framework for the 
frontend. 
Mention: This application can also be deployed on a web server, allowing anyone to use it without any specific setup installed on its system.

## Environment Setup

Install 'Tailwind CSS' by downloading the appropriate executable file for your OS available on: 
[Tailwind CSS v3.4.13 Release](https://github.com/tailwindlabs/tailwindcss/releases/tag/v3.4.13). Then, rename the file and add it to the system PATH to access it 
from anywhere across your computer.

Next, install the required dependencies:

-  ``$ pip install Flask``
-  ``$ pip install openai``
-  ``$ pip install python-dotenv``

To enable an interaction between ChatGPT and Skydel, download the Skydel Remote API by following the instructions 
provided on the public GitHub repo : [Skydel Remote API repository](https://github.com/learn-safran-navigation-timing/skydel-remote-api). 
Make sure that the Skydel RAPI is properly installed by running the `basic_exemple.py` script available on the same repo.

## Usage

1. Generate an API key from the [OpenAI website](https://platform.openai.com/signup), and assign it to the `openai.api_key` variable.
2. Run `app.py` using any code editor or terminal (make sure that Python is installed and added to your system PATH).
3. Open your web browser and navigate to `http://127.0.0.1` to access the local hoisted application.

Once the application is running, you should be able to send/receive messages from ChatGPT via the GUI.

