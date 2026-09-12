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
    response :ChatResponse = chat(model="deepseek-r1:1.5b",messages=[{
        'role' : 'user',
        'content': f'ok erstelle mir einen suchanfragen text zum thema "{contex[1].text}". Gebe nur die auchanfrage text OHNE weitere erklärungen oder gedanken weg. Ignoriere dabei die anfragen von mir davor. Denke nicht zu viel nach. Suche selber aber nicht dabei, sondern gebe nur den suchtext an ohne dabei selber dannach zu suchen.'
    }])

    return(response.message.content)