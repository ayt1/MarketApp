from .market_class import Market
import requests
from bs4 import BeautifulSoup
import re
from copy import deepcopy


class Sok(Market):
    def __init__(self, market_config):
        super().__init__(market_config)

    def fetch_discount_brochures(self):
        response = requests.get(self.main_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        # Use a partial class match to find the container div
        containers = soup.find_all('div', class_=lambda c: c and c.startswith("Catalog_catalogContainer"))
        container = containers[0]

        anchor_tags = container.find_all('a', href=True)
        for a_tag in anchor_tags:
            match = re.search(r'/(\d{1,2}_[a-zA-Z]+_\d{1,2}_[a-zA-Z]+)', a_tag['href'])
            if not match:
                match = re.search(r'/(\d{1,2}_\d{1,2}_[a-zA-Z]+)', a_tag['href'])
                tarih = match.group(1).split('_')
                tarih = f"{tarih[0]}-{tarih[1]} {self.fix_month_name(tarih[-1])}"
            else:
                tarih = match.group(1).split('_')
                tarih = f"{tarih[0]} {self.fix_month_name(tarih[1])} - {tarih[2]} {self.fix_month_name(tarih[-1])}"

            self.indirim_dict['tarih'] = tarih
            self.indirim_dict['pdf_url'] = [a_tag['href']]
            self.indirim_dict['title'] = a_tag['title']
            self.indirim_dict['thumbnail'] = self.indirim_dict['pdf_url']
            self.output['indirimler'].append(deepcopy(self.indirim_dict))

        return self.output
