import requests
from bs4 import BeautifulSoup
from .market_class import Market


class HappyCenter(Market):
    def __init__(self, market_config):
        super().__init__(market_config)

    def fetch_discount_brochures(self):
        response = requests.get(self.main_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        images = soup.find_all('img', class_="resim img-responsive")
        self.indirim_dict['title'] = "İndirim Bülteni"
        self.indirim_dict['image_urls'] = [image['src'] for image in images]
        self.indirim_dict['thumbnail'] = self.indirim_dict['image_urls'][0]
        self.indirim_dict['pdf_url'] = self.save_as_pdf(self.indirim_dict['image_urls'], self.save_dir)
        self.output['indirimler'].append(self.indirim_dict)

        return self.output

