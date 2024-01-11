import asyncio
import g4f

from pywebio.input import input
from pywebio.output import put_text
from pywebio import start_server

messages = []

def ask_gpt(messages: list) -> str:
    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_35_turbo,
        messages=messages
    )
    put_text(response)    
    return response



def main():
    messages = []
    messages.append({"role": "user", "content": input("Введите ваш вопрос к чатGPT:")})
    messages.append({"role": "assistant", "content": ask_gpt(messages=messages)})

    

if __name__ == "__main__":
    start_server(main, debug=True, port=8080, cdn=False)

