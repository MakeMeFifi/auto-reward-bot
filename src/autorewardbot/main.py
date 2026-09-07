from selenium import webdriver
from rich.console import Console
import pyfiglet
from .login import manageLogIn

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

options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")

driver:webdriver.Edge = webdriver.Edge(options=options) 



def main():
    console.print(f"[bold green] {title} [/bold green] \n [bold yellow] created by MakeMeFifi [/bold yellow]")
    manageLogIn(driver,console)
    console.print("[bold green] opening reward page [/bold green]")
    driver.get(SITE)
    input()
    
