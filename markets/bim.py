from copy import deepcopy
import requests
from bs4 import BeautifulSoup
from .market_class import Market
import re


class BIM(Market):
    def __init__(self, market_config):
        super().__init__(market_config)
        self.swiper_xpath = '//*[@id="form1"]/div/div[2]/div/div/div/div[3]'


    def fetch_discount_brochures(self):
        try:
            regex_pattern = r'\d{2}-\d{2}'
            response = requests.get(self.main_url)
            soup = BeautifulSoup(response.text, 'html.parser')

            dates = soup.find_all('a', class_='subTabArea triangle')
            image_sections = soup.find_all('div', class_='smallArea col-4 col-md-3')
            dates.reverse()
            image_sections.reverse()

            for date, section in zip(dates, image_sections):
                date = date.text.strip()
                self.indirim_dict['tarih'] = date
                match = re.match(regex_pattern, date)
                title = "İndirimli Ürünler" if match else "Bim Aktüel"
                self.indirim_dict['title'] = title
                images_info = section.find_all('a', class_='small')
                self.indirim_dict['image_urls'] = [img['data-bigimg'] for img in images_info]
                self.indirim_dict['pdf_url'] = self.save_as_pdf(self.indirim_dict['image_urls'], self.save_dir)
                self.indirim_dict['thumbnail'] = self.indirim_dict['image_urls'][0]

                self.output['indirimler'].append(deepcopy(self.indirim_dict))

            return self.output

        except Exception as e:
            print(e)
            return self.output