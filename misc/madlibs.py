#!/usr/bin/env python3

name: str = input("Enter a name: ")
noun_a: str = input("Enter a noun: ")
noun_b: str = input("Enter a noun: ")
verb_a: str = input("Enter a verb: ")
verb_b: str = input("Enter a verb (past tense): ")
number_a: str = input("Enter a number: ")
number_b: str = input("Enter another number: ")

story: str = f"""
----------------------------------------------------------------------------------------------------------------------------
This is a story about {name}, a strong and beautiful hamster/{noun_a}, with their trusty steed, Kapua, who loved to {verb_a}.

{name} once {verb_b} and won a {noun_b} as a prize.
Isn't that cool???

Anyways,
Today, {name} is {int(number_a) + int(number_b)} years old, and is now retired from these crazy adventures.
However, some say, one day they will return...
----------------------------------------------------------------------------------------------------------------------------
"""

print(story)
