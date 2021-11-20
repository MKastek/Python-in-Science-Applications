from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service('/Users/marcinkastek/.wdm/drivers/chromedriver/mac64/95.0.4638.69/chromedriver')
driver = webdriver.Chrome(service=service)

# get site
driver.get('http://www.fizyka.pw.edu.pl/index.php/Pracownicy/Lista-pracownikow/Pracownicy-badawczo-dydaktyczni')

elements = driver.find_elements(By.CSS_SELECTOR,'h2, h2 + div')
for element in elements:
    print(element.text)

#time.sleep(5)
driver.close()
