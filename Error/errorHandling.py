#!/usr/bin/env python3

user_input : str = "10"

try:
    result: float = 1 / float(user_input)
    print(f"1 / {user_input} = {result}")

except ValueError:
    print(f"You cannot use {user_input} as a value.")

except ZeroDivisionError:
    print("You cannot ")

else:
    print("No errors detected!!!")

finally:
    print("This is always executed.")
