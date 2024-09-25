import openai
import os

openai.api_key = os.environ.get("OPENAI_API_KEY")

prompt = "Hello! How are you?"

def get_response(prompt):
    try:
        completion = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return completion.choices[0].message['content']
    except Exception as e:
        return f"Une erreur s'est produite: {str(e)}"

print(get_response(prompt))