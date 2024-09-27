
function _cloneAnswerBlock() { // Clone answer block to generate a conversation historic

    const output = document.querySelector("#gpt-output"); // Represents the div where message will be cloned
    const template = document.querySelector('#chat-template');  // Template to clone
    const clone = template.cloneNode(true);  // Cloning function
    clone.id = "";  // Re-initializing the id of the chat template to not clone the same text twice
    output.appendChild(clone); // Adding the clone on the wanted div
    clone.classList.remove("hidden") // Removing the hidden parameter to display the template once cloned
    return clone.querySelector(".message"); // Recovering all the element with the message class
}

function addToLog(message) {
    // Add the message to clone
    const infoBlock = _cloneAnswerBlock(); // Bloc creation

    if (!infoBlock) {
        console.error("Échec de la création du bloc d'information");
        return null;
    }

    infoBlock.innerText = message;  // Add the message to the cloned block
    return infoBlock;
}

function getChatHistory() {
    // Recovering the whole chat (important to send all the conversation to GPT to give him some context)
    const infoBlocks = document.querySelectorAll(".message:not(#chat-template .message)");  // Select all the messages while excluding the HTML template

    if (!infoBlocks.length) {
        console.warn('Aucun bloc d\'information trouvé');
        return [];
    }
    return Array.from(infoBlocks).map(block => block.innerHTML); // Recovering only the text in the block
}

async function fetchPromptResponse(prompt) {
    // Interfacing the frontend with the backend
    const response = await fetch("/prompt", {  // Sending a fetch request to recover backend data
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({messages: getChatHistory()}),
    });
    return response.body.getReader();
}

async function readResponseChunks(reader, gptOutput) {
    const decoder = new TextDecoder();
    const converter = new showdown.Converter();

    let chunks = "";
    while (true) {
        const {done, value} = await reader.read();
        if (done) {
            break;
        }
        chunks += decoder.decode(value);
        gptOutput.innerHTML = converter.makeHtml(chunks);
    }
}

document.addEventListener("DOMContentLoaded", () => {
    // Event listener to check if the HTML sheet is completely generated, if yes:
    const form = document.querySelector("#prompt-form");  // Recovering the form
    const spinnerIcon = document.querySelector("#spinner-icon");
    const sendIcon = document.querySelector("#send-icon");

    form.addEventListener("submit", async (event) => {  // New event listener on the click on the submit button
        event.preventDefault(); // Prevent default form submission
        spinnerIcon.classList.remove("hidden"); // Displaying the spinner icon
        sendIcon.classList.add("hidden"); // Hide the send icon

        const prompt = form.elements.prompt.value; // Recovering the value of the input (the text)
        form.elements.prompt.value="";
        addToLog(prompt); // Sending the text value to the function to display it into the block answer

        try {
            //const gptOutput = addToLog("GPT est en train de réfléchir...");
            const reader = await fetchPromptResponse(prompt);
            //await readResponseChunks(reader, gptOutput);
        } catch (error) {
            console.error('Une erreur est survenue:', error);
        } finally {
            spinnerIcon.classList.add("hidden");
            sendIcon.classList.remove("hidden");
            hljs.highlightAll();
        }
    });
});
