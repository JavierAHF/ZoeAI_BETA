from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def search(something):
    browser = webdriver.Chrome(executable_path='C:\\Chromedriver\\chromedriver.exe')
    browser.maximize_window()
    browser.get('https://www.google.com/')
    findElem = browser.find_element_by_name('q')
    findElem.send_keys(something)
    findElem.send_keys(Keys.RETURN)