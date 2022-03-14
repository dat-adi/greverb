from rich import print
from rich.panel import Panel
from rich.text import Text
from rich.console import Console

from random import randint
from time import sleep
import json


def prompt(pair):
    """Providing a word, and then the definition"""
    word = Panel(Text(pair[0], justify="center", style="bold magenta"))
    definition = Panel(Text(pair[1], justify="center"))

    console = Console()
    with console.screen():
        console.print(word)
        sleep(5)
        console.print(definition)
        sleep(5)

def random_word(word_data, limit):
    """Picking from the JSON word list"""
    ran_no = randint(0, limit)
    random_word = word_data[ran_no]
    return (random_word["word"], random_word["definition"])

if __name__ == "__main__":
    try:
        with open("./data/word_list.json") as f:
            data = json.load(f)
            while True:
                pair = random_word(data, 1162)
                prompt(pair)
    except KeyboardInterrupt:
        print("Well, that's something. Do something.")
