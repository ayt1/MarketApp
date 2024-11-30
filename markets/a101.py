from copy import deepcopy
from selenium import webdriver
from .market_class import Market
import time
from selenium.webdriver.common.by import By


class A101(Market):
    def __init__(self, market_config):
        super().__init__(market_config)
        self.cookie_button_xpath = '//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]'
        self.container_xpath = '/html/body/div/div[2]/div[2]/div/div/div'
        self.swiper_xpath = '/html/body/div/div[2]/div/div/div[3]/div/div[1]/div'
        self.driver = webdriver.Chrome(options=self.chrome_options)


    def fetch_discount_brochures(self):
        afis_ismi = {"0": "Haftanın Yıldızları",
                     "1": "Aldın Aldın",
                     "2": "Aldın Aldın",
                     "3": "Büyük Olduğu İçin Ucuz"
                     }
        sub_driver = webdriver.Chrome(self.chrome_options)
        try:
            self.driver.get(self.main_url)
            time.sleep(2)
            tags_container = self.driver.find_elements(By.XPATH, self.container_xpath)[0]
            tags = tags_container.find_elements(By.TAG_NAME, 'a')
            for i, tag in enumerate(tags[:-1]):
                tag_url = tag.get_attribute('href')
                tag_date = tag.find_element(By.TAG_NAME, 'span').text
                self.indirim_dict['tarih'] = tag_date
                self.indirim_dict['title'] = afis_ismi[str(i)]
                sub_driver.get(tag_url)
                time.sleep(1)
                swiper = sub_driver.find_elements(By.XPATH, self.swiper_xpath)[0]
                images = swiper.find_elements(By.TAG_NAME, 'img')
                image_urls = [image.get_attribute('src') for i, image in enumerate(images) if image.get_attribute('src') and i%2==0]
                image_urls = image_urls[1:-1]

                self.indirim_dict["image_urls"] = list(image_urls)
                self.indirim_dict['thumbnail'] = self.indirim_dict['image_urls'][0]
                self.indirim_dict['pdf_url'] = self.save_as_pdf(self.indirim_dict['image_urls'], self.save_dir)
                self.output["indirimler"].append(deepcopy(self.indirim_dict))


            self.driver.quit()
            sub_driver.quit()

            return self.output
        finally:
            self.driver.quit()
