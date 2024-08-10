#!/usr/bin/env python3

numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8]

print(numbers[::3])

people: list[str] = ["Anna", "Bob", "Chris", "David", "Fred"]

for person in people:
    print(f'- {person}, {people.index(person)}')

    if person == 'Bob':
        print(f'Removing: {person}')
        people.remove('Bob')
