from selenium import webdriver

driver:webdriver.Edge = webdriver.Edge()
testDrive:webdriver.Firefox = webdriver.Firefox()

def main() ->None :
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    testDrive.get("https://www.selenium.dev/selenium/web/web-form.html")
    print(f"{driver.title} is from edge and \n {testDrive.title} is from firefox")