from selenium import webdriver

options = webdriver.EdgeOptions()

options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")

driver:webdriver.Edge = webdriver.Edge(options=options) 

def main() ->None :
    driver.get("https://bing.com")
    input("press anything to close the window")