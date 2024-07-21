#!/usr/bin/env python3
import sys
from datetime import datetime

def get_response(text: str, name: str) -> str:
    lowered: str = text.lower()

    userGreetings = ["hi", "hello", "hey"]
    userFarewells = ["bye", "goodbye"]

    match lowered:

        case lowered if lowered in userGreetings:
            return f"Sup, {name}, your'e a bro!"

        case lowered if "how are you" in lowered:
            return "I\'m good bro!"

        case lowered if "your name" in lowered:
            return "My name is: ChadBot"

        case lowered if "time" in lowered:
            current_time: datetime = datetime.now()
            return f"The time is: {current_time:%H:%M}"

        case lowered if lowered in userFarewells:
            return "I'll see you later! *mews*"

        case _:
            return f"Sorry, I wasn't trying to mog you bro, I don't understand '{text}'"

userName = input("Please enter your name: ")

while True:
    user_input: str = input('You: ')

    if user_input == "exit":
        print("Bot: It was a pleasure talking bro.")
        sys.exit()

    bot_response: str = get_response(user_input, userName)
    print(f"Bot: {bot_response}")
