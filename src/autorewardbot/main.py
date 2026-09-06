from selenium import webdriver
from rich.console import Console
import pyfiglet

console: Console = Console()
title = pyfiglet.figlet_format("Auto Reward Bot", font="pagga")
driver:webdriver.Edge = webdriver.Edge()    # Opens the edge window


def main():
    console.print(f"[bold green] {title} [/bold green] \n [bold yellow] created by MakeMeFifi [/bold yellow]")

