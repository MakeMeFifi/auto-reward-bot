from selenium.webdriver.remote.webelement import WebElement
from selenium import webdriver
from selenium.webdriver.common.by import By
from humancursor import WebCursor
from ollama import chat
from ollama import ChatResponse

def doBingExplore(driver:webdriver.Edge, cursor:WebCursor)->None:
    startTab = driver.current_window_handle
    parent = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/main/section[2]/div/div[2]/div/div")
    children = parent.find_elements(By.CSS_SELECTOR, ":scope > *")
    a_list:list[WebElement] = []
    # gets all clickable elements
    for e in children:
        if (e.tag_name.lower() == "a"):
            a_list.append(e)
    
    for element in a_list:
        content:list[WebElement] = element.find_elements(By.XPATH, ".//p")
        print(get_search_query(content))


    return


def get_search_query(contex:list[WebElement])->str:
    prompt = f"""Wandle den Text in einen kurzen Bing-Suchbegriff um.

    Text: Suchen Sie auf Bing nach atemberaubendem Schmuck für jeden Anlass
    Suchbegriff: schmuck für jeden anlass kaufen

    Text: Finde heraus wie das Wetter morgen in München wird
    Suchbegriff: wetter morgen münchen

    Text: Überprüfen Sie wer gestern das Champions League Spiel gewonnen hat
    Suchbegriff: gewinner champions league gestern

    Text: {contex[1].text}
    Suchbegriff:"""

    response: ChatResponse = chat(
        model="qwen2.5:0.5b",
        messages=[{'role': 'user', 'content': prompt}],
        options={'temperature': 0.1}  # Wichtig: niedrige Temperatur verhindert Halluzinationen
    )

    # Sauberes Auslesen der ersten Zeile + Entfernen von Restzeichen
    suchbegriff = response.message.content.strip().split('\n')[0].replace('"', '').replace("'", "").strip()

    return suchbegriff