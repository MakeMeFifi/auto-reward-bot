from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.common.by import By
from rich.console import Console
import pyfiglet
from pathlib import Path
from humancursor import WebCursor
from .dailyTasks import getAllDailyTasks

"""
TODO:
    1. Login (done)
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

#Adding arguments to hide flags that reveal that the browser is managed by a bot
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")

#Adding directory where the local cookies are stored
options.add_argument(f"--user-data-dir={PATH}")

driver:webdriver.Edge = webdriver.Edge(options=options) 
cursor:WebCursor = WebCursor(driver)



def main():
    console.print(f"[bold green] {title} [/bold green] \n [bold yellow] created by MakeMeFifi [/bold yellow]")
    console.print("[bold green] opening reward page [/bold green]")
    if not PATH.exists():
        console.print("[bold red]Youre not Logged in, please log in your Microsoft Account and Press Enter after youre done [/bold red]")
        driver.get("https://bing.com")
        input()
    driver.get(SITE)

    #beginning with daily tasks
    console.print("[bold white] [1] [/bold white][bold blue] - beginning with doing the daily tasks [/bold blue]")
    cursor.click_on(driver.find_element(By.ID, "react-aria-_R_3dalav5t6bslbH1_"))
    getAllDailyTasks(driver,cursor)
    console.print("[bold green] Daily tasks done! [/bold green]")

    #debug
    input()

