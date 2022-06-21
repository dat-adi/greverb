from rich import print
from rich.panel import Panel
from rich.text import Text
from rich.console import Console
from rich.prompt import Prompt

from random import randint
from time import sleep
import json

def random_word(words):
    """Picking from the word list"""
    return randint(0, len(words))

def retrieval():
    """Method to retrieve elements from the text file"""
    with open("./data/violet_cards.txt") as f:
        lines = f.readlines()

    words: list = []
    meanings: list = []
    examples: list = []
    for line in lines:
        split_up = line.split("::")
        words.append(split_up[0][2:-1])
        split_up_meaning_and_example = split_up[1].split(".")
        meanings.append(split_up_meaning_and_example[0][1:])
        examples.append(split_up_meaning_and_example[1][1:])

    return words, meanings, examples

def prompt(word, meaning, example):
    """The prompt for the guessing"""
    word = Panel(Text(word, style="bold magenta"))
    meaning = Panel(Text(meaning))
    example = Panel(Text(example))

    console = Console()
    with console.screen():
        console.print(word)
        user_meaning = Prompt.ask("Enter your guess for the meaning")
        console.clear()
        console.print(word)
        console.print(meaning)
        user_meaning = Panel(Text(user_meaning))
        console.print(user_meaning)
        console.print(example)
        sleep(5)

if __name__ == "__main__":
    """Main function for guessing"""
    words, meanings, examples = retrieval()
    number = random_word(words)
    prompt(words[number], meanings[number], examples[number])
