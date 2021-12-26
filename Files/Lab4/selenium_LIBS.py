from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import matplotlib.pyplot as plt
import time


class SimulatedLIBS(object):

    def __init__(self, Te=1.0, Ne=10 ** 17, elements=None, percentages=None, resolution=6000, low_w=300, upper_w=301,
                 max_ion_charge=3):

        self.Te = Te
        self.Ne = Ne
        self.elements = elements
        self.percentages = percentages
        self.resolution = resolution
        self.low_w = low_w
        self.upper_w = upper_w
        self.max_ion_charge = max_ion_charge

        self.retrieve_data()

    def retrieve_data(self):

        composition = ""
        spectrum = ""

        for i in range(len(self.elements)):
            if i > 0:
                composition += "3B"
                spectrum += "2C"
            composition += str(self.elements[i])
            composition += "%3A"
            composition += str(self.percentages[i])

            spectrum += str(self.elements[i])
            spectrum += "0-" + str(self.max_ion_charge)

            if i < len(self.elements) - 1:
                composition += "%"
                spectrum += "%"
        site = "https://physics.nist.gov/cgi-bin/ASD/lines1.pl?composition={}" \
               "&spectra={}" \
               "&low_w={}&limits_type=0&upp_w={}" \
               "&show_av=3&unit=1" \
               "&resolution={}" \
               "&temp={}" \
               "&eden={}" \
               "&maxcharge={}" \
               "&min_rel_int=0.01" \
               "&libs=1"
        site = site.format(composition, spectrum, self.low_w, self.upper_w, self.resolution, self.Te, self.Ne,
                           self.max_ion_charge)

        service = Service('/Users/marcinkastek/.wdm/drivers/chromedriver/mac64/95.0.4638.69/chromedriver')
        driver = webdriver.Chrome(service=service)

        driver.get(site)
        time.sleep(2)

        search_bar = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH,"/html/body/div/div[1]/div[1]/form/div[3]/div/input")))
        search_bar.clear()
        search_bar.send_keys('1000')

        recalculate_button = WebDriverWait(driver,2).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/div[1]/div[1]/form/button")))
        recalculate_button.click()


        list = driver.find_element(By.XPATH,"/html/body/div/div[2]/div[1]/div/div[1]/div/div/table/tbody").find_elements(By.TAG_NAME, "tr")


        wavelength = []
        intensity = []

        for l in list:
            data = l.find_elements(By.TAG_NAME, "td")
            wavelength.append(float(data[0].get_attribute("textContent")))
            intensity.append(float(data[1].get_attribute("textContent").replace(",","")))

        driver.close()
        plt.plot(wavelength,intensity)
        plt.show()







spectra = SimulatedLIBS(elements=['Ar','Ti'],percentages=[99.9,0.1])
