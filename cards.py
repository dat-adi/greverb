from rich.text import Text
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table

from random import randint
from time import sleep

def random_word(words):
    """Picking from the word list"""
    return randint(0, len(words))

def retrieval():
    """Method to retrieve elements from the text file"""
    with open("./data/violet_cards.org") as f:
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
    word = Text(word, style="bold magenta")
    meaning = Text(meaning)
    example = Text(example)

    table = Table(title=word)
    table.add_column("Type", style="cyan")
    table.add_column("Meaning", style="magenta")
    table.add_column("Example", style="green", no_wrap=True)

    table.add_row("From the Source", meaning, example)

    console = Console()
    with console.screen():
        console.print(f"The word is \"{word}\"")
        user_meaning = Prompt.ask("Enter your guess for the meaning")
        user_meaning = Text(user_meaning)
        table.add_row("Your response", user_meaning, "-")
        console.clear()
        console.print(table)
        sleep(5)

if __name__ == "__main__":
    """Main function for guessing"""
    words, meanings, examples = retrieval()
    number = random_word(words)
    prompt(words[number], meanings[number], examples[number])
