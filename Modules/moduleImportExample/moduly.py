#!/usr/bin/env python3

from typing import Final

AUTHOR: Final[str] = "Charles"
VERSION: Final[int] = 1


def greet(name: str) -> None:
    print(f'Hello, {name}!')
