from time import sleep

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://automationexercise.com")

register_button = driver.find_element("xpath", "//a[contains(text(), 'Signup')]")
register_button.click()
sleep(5)

