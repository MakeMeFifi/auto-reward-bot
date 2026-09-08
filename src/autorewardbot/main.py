from selenium import webdriver
from rich.console import Console
import pyfiglet
from pathlib import Path

"""
TODO:
    1. Login
    2. Automating

Reward Goals:
    1. Search streak
    2. set Streak
    3.bing explore
    4. more options
    5. Dashboard free points

"""
console: Console = Console()
title = pyfiglet.figlet_format("Auto Reward Bot", font="pagga") # Opens the edge window
options = webdriver.EdgeOptions()
SITE = "https://rewards.bing.com/earn"
PATH = Path(__file__).resolve().parent.parent / "edge_profile"

options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument(f"--user-data-dir={PATH}")

driver:webdriver.Edge = webdriver.Edge(options=options) 



def main():
    console.print(f"[bold green] {title} [/bold green] \n [bold yellow] created by MakeMeFifi [/bold yellow]")
    console.print("[bold green] opening reward page [/bold green]")
    if not PATH.exists():
        console.print("[bold red]Youre not Logged in, please log in your Microsoft Account and Press Enter after youre done [/bold red]")
        driver.get("https://bing.com")
        input()
    driver.get(SITE)
    input()
    
