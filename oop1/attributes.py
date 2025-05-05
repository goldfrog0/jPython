#!/usr/bin/env python3

class Animal:
    tricks: list[str] = []

    def __init__(self, name) -> None:
        self.name = name

    def teach_trick(self, trick_name: str) -> None:
        self.tricks.append(trick_name)

def main() -> None:
    cat = Animal("yuki")
    dog = Animal("kapua")

    cat.teach_trick('Wash dishes')
    cat.teach_trick('clean car')
    print(cat.tricks)


if __name__ == "__main__":
    main()
