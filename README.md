# Sky-GPT

## Project Objectives
The objective is to develop an application to interface OpenAI's ChatGPT with Skydel to create and run simulation
automatically, based on the user’s requirements specified on the prompt. This application would help any skydel user 
to easily create various testing scenarios to assess the performance of a GNSS receiver under different conditions.

## Technical details
Sky-GPT integrates OpenAI's ChatGPT through its Python API to automate the simulation configuration and running on the Skydel software. 
This project can be deployed on any web server, allowing user to use without needing any specific local setup. If you want to run it locally, 
you'll need to install `Flask` framework for the python backend. The frontend is managed using the `Tailwind CSS` framework and JavaScript.

## Environment Setup

Install 'Tailwind CSS' by following the link: [Tailwind CSS v3.4.13 Release](https://github.com/tailwindlabs/tailwindcss/releases/tag/v3.4.13) 
and download the appropriate executable depending on your OS. After downloading, rename the file and add its path as an 
environment variable to access it from anywhere across your machine.

Next, install the required dependencies:

``$ pip install Flask``
``$ pip install openai``
``$ pip install python-dotenv``

To enable an interaction between ChatGPT and Skydel, download the Skydel Remote API by following the instructions 
provided in the GitHub : [Skydel Remote API repository](https://github.com/learn-safran-navigation-timing/skydel-remote-api). 
Ensure that the Skydel RAPI is properly installed and configured, allowing ChatGPT to execute commands and manage simulations in Skydel.

## Usage

1. Generate an API key from the [OpenAI website](https://platform.openai.com/signup), and assign it to the `openai.api_key` variable.
2. Run `app.py` using any code editor or terminal.
3. Open your web browser and navigate to `http://127.0.0.1` to access the local hoisted application.

Once the application is running, you should be able to send/receive messages from ChatGPT via the GUI.

