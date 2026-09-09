from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait                                                                  
from selenium.webdriver.support import expected_conditions as EC   
from humancursor import WebCursor
import time

def getAllDailyTasks(driver:webdriver.Edge,cursor:WebCursor) -> None:
    #saves the tab where the reward page is open
    startTab = driver.current_window_handle
    wait = WebDriverWait(driver, 10)

    #waits until the side pannel is open
    parent = wait.until(
            EC.presence_of_element_located((By.XPATH, "//*[starts-with(@id, 'react-aria')]/div/div[2]/div/div[2]"))          
        )
    elements = parent.find_elements(By.CSS_SELECTOR, ":scope > *")

    #goes through every tasks and click on it
    for element in elements:
        cursor.click_on(element)
        time.sleep(2)
        driver.switch_to.window(startTab)
    
    #closing the side panel
    cursor.click_on(driver.find_element(By.XPATH, "/html/body/div[3]/div/section/div/div[1]/button"))
    return
