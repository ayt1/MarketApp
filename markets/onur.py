from copy import deepcopy
import re
import requests
from bs4 import BeautifulSoup
from .market_class import Market


class Onur(Market):
    def __init__(self, market_config):
        super().__init__(market_config)
        self.catalog_name_xpath = '/html/head/meta[7]'

    def fetch_discount_brochures(self):
        try:
            response = requests.get(self.main_url)
            soup = BeautifulSoup(response.text, 'html.parser')
            pattern_1 = r'\d{1,2} [A-Za-zğıŞü]+ - \d{1,2} [A-Za-zğıŞü]+ \d{4}'
            pattern_2 = r'\d{1,2}-\d{1,2} [A-Za-zğıŞü]+ \d{4}'
            catalogs = soup.find_all('div', class_='katalogTxt')
            for catalog in catalogs:
                self.indirim_dict['title'] = catalog.h3.text
                date = re.search(pattern_1, catalog.span.text)
                if not date:
                    date = re.search(pattern_2, catalog.span.text).group(0)
                else:
                    date = date.group(0)
                self.indirim_dict['tarih'] = date
                pdf_url = catalog.find('a', class_='katalogİnceleBtn')['href']
                self.indirim_dict['pdf_url'] = self.save_as_pdf([pdf_url], self.save_dir)
                self.indirim_dict['thumbnail'] = self.indirim_dict['pdf_url']

                self.output['indirimler'].append(deepcopy(self.indirim_dict))

            return self.output
        except Exception as e:
            print(str(e))
            return self.output



