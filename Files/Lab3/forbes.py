import requests as re
from bs4 import BeautifulSoup
import pandas as pd


class Forbes:

    def __init__(self, site):
        self.site = site
        self.forbes_dict = {'Firma': [], 'Siedziba': [],'Branża': [], 'Sprzedaż 2019': [],'Zysk': [], 'Średnia': []}
        self.webscrapping(self.site)

    def webscrapping(self, site):
        req = re.get(site)
        soup = BeautifulSoup(req.text, 'html.parser')
        div = soup.find('div', class_='tableWrapper')
        divs = div.find_all('td')

        for div in divs:
            for name in self.forbes_dict.keys():
                if str(div).find(name) != -1:
                    self.forbes_dict[name].append(div.text.strip())
        self.forbes_df = pd.DataFrame(self.forbes_dict)

    def print(self):
        print(self.forbes_df)
