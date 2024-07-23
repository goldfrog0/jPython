#!/usr/bin/env python3

import string

def is_only_letters(user_input: str) -> None:

    alphabet = string.ascii_letters + " "
    for char in user_input:
        if char not in alphabet:
            raise ValueError("Text can only contain letters from the english alphabet!")

    print(f'"{user_input}" is letters only, good job playa.')

def main() -> None:

    while True:
        try:
            user_input: str = input("Check text: ")
            is_only_letters(user_input)
        except ValueError:
            print("Please only enter English letters...")
        except Exception as e:
            print(f"Encountered an unknown exception: {type(e)} {e} ")


main()
