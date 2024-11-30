import time
from copy import deepcopy
from selenium import webdriver

from selenium.webdriver.common.by import By

from .market_class import Market

class Watsons(Market):
    def __init__(self, market_config):
        super().__init__(market_config)
        self.catalog_name_xpath = '/html/head/meta[7]'
        self.driver = webdriver.Chrome(options=self.chrome_options)

    def fetch_discount_brochures(self):
        self.driver.get(self.main_url)
        time.sleep(2)
        catalog_name = self.driver.find_element(By.XPATH, self.catalog_name_xpath).get_attribute('content')
        pdf_url = self.driver.find_elements(By.ID, 'downloadAsPdf')[0].get_attribute('href')
        self.indirim_dict['pdf_url'] = self.save_as_pdf([pdf_url], self.save_dir)
        self.indirim_dict['title'] = catalog_name
        self.indirim_dict['thumbnail'] = self.indirim_dict['pdf_url']
        self.output['indirimler'].append(deepcopy(self.indirim_dict))

        self.driver.quit()

        return self.output


