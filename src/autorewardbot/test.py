from selenium import webdriver

driver:webdriver.Firefox = webdriver.Firefox()

def main() ->None :
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    print(driver.title)