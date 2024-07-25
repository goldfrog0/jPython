#!/usr/bin/env python3

import requests
from requests import Response


def get_response(url: str) -> Response:
    return requests.get(url)


def show_response_info(response: Response) -> None:
    print(f"Status: {response.status_code}")
    print(f"OK: {response.ok}")
    print(f"Links: {response.links}")
    print(f"Encoding: {response.encoding}")
    print(f"Is_redirect: {response.is_redirect}")
    print(f"Is_perm_redirect: {response.is_permanent_redirect}")


def main() -> None:
    while True:
         try:
             website: str = input("Website url: ")
             response: Response = get_response(website)
             show_response_info(response)
             break

         except:
             print("Invalid Website url, try again.")


if __name__ == "__main__":
    main()
