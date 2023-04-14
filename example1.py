# python -m pip install selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


driver = webdriver.Chrome("/Users/samoy/SkillfactoryProjects/Python_selenium_skill/chromedriver")
driver.get("https://google.com")
driver.find_element(By.XPATH, "//input[@title=\"Поиск\"]").send.keys('Skillfactory' + Keys.RETURN)
sleep(2)
driver.save_screenshot('sf.png')
driver.quit()