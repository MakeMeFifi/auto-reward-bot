from selenium import webdriver
from pathlib import Path
import json
from rich.console import Console

PATH = Path("Cookies.json")
SITE = "https://rewards.bing.com/earn"

def manageLogIn(driver: webdriver.Edge, console : Console) -> None:
    console.print(f"[bold white] checking for JSON data [/bold white] ")
    if(PATH.exists()):
        console.print("[bold green] Cookies.json found \n beginn loading cookies information into the browser[/bold green]")
        driver.get("https://bing.com")
        with(open(PATH, "r")) as f:
            cookies = json.load(f)
            for c in cookies:
                try:
                    driver.add_cookie(c)
                except Exception as e:
                    pass
        console.print("[bold green] JSON file loaded succsesfully[/bold green]")
        driver.refresh()
        return
    else:
        console.print("[bold red]JSON file not found, pls log into your microsoft Account to create the nessesary cookies. [/bold red]")
        driver.get("https://login.live.com")
        console.print("[bold yellow] after you logged in, press in the Terminal ENTER to confirm it [/bold yellow]")  
        input()

        createJSON(driver)
        console.print("[bold green] JSON file succsessfully created [/bold green]")
        return
            

def createJSON(driver: webdriver.Edge): 
    driver.get("https://bing.com")
    cookies = driver.get_cookies()
    with(open(PATH, "x")) as f:
        json.dump(cookies,f,indent=4 )

    driver.refresh()
    return