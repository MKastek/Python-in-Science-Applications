from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

service = Service('/Users/marcinkastek/.wdm/drivers/chromedriver/mac64/95.0.4638.69/chromedriver')
driver = webdriver.Chrome(service=service)
driver.get('http://www.fizyka.pw.edu.pl')
time.sleep(5)
driver.close()
