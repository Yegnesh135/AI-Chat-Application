import os
import requests
from typing import List
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
openai = OpenAI()

def stream_chat(prompt,conversation_history):
    
    if not conversation_history:
        system_message = """You are an AI assistant named Yegnesh AI an excellent orator assisting the user in all their queries technically in a clear way in such a way 
        that the user can understand it easily and can apply it or make use of it at the time of need."""
        conversation_history = [{"role": "system", "content": system_message}]
    
    conversation_history.append({"role": "user", "content": prompt})



    response = openai.chat.completions.create(
    model="gpt-4.1-2025-04-14",
    messages=conversation_history,
    stream=True,  # Set to True if you want to stream the response
    )

    full_response = ""
    for chunk in response:
        if chunk.choices[0].delta.content:
            chunk_content = chunk.choices[0].delta.content
            full_response += chunk_content
            yield full_response
    conversation_history.append({"role": "assistant", "content": full_response})


    

if __name__ == "__main__":
    print(50*"-")
    result = stream_chat("Hello, how can I help you?", [])
    print(result)
