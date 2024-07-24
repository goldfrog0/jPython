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
    website: str = "https://www.indently.io/abc"
    response: Response = get_response(website)
    show_response_info(response)

if __name__ == "__main__":
    main()
