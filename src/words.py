"""Module for handling list of words"""
import random
import requests
import json
from typing import List

def save_json(words: List[str], filename: str) -> None:
    with open(filename, "w", encoding="UTF-8") as file:
        json.dump(words, file)

def open_json(filename: str) -> List[str]:
    with open(filename, "r", encoding="UTF-8") as file:
        data = json.load(file)
    return data

def get_words(length: int = 5, amount: int = 100000) -> List[str]:
    url = f"https://random-word-api.herokuapp.com/word"
    params = {
        "length": length,
        "number": amount
    }
    response = requests.get(url, params=params)
    if response.status_code != 200:
        raise requests.exceptions.HTTPError(f"Request failed with status code: {response.status_code}")
    words = response.json()
    if words == []:
        raise ValueError(f"No words found with length {length}")
    return words

def get_random_word(source: str = "WEB") -> str:
    match source:
        case "WEB":
            return get_words(amount=1)
        case "FILE":
            words = open_json("assets/words.json")
            return random.choice(words)
        case _:
            raise ValueError(f"Unsupported source {source}")


def main() -> int:
    words = get_words()
    return 0

if __name__ == "__main__":
    SystemExit(main())