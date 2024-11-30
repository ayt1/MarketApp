import difflib
import os
import time
from io import BytesIO
from uuid import uuid4

import requests
from PIL import Image
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class Market(object):
    def __init__(self, market_config):
        self.main_url = market_config["main_url"]
        self.output = market_config["output_json"]
        self.indirim_dict = {"title": "", "tarih": "", "image_urls": [], "thumbnail": "", "pdf_url": ""}
        self.chrome_options = Options()
        self.chrome_options.add_argument("--start-fullscreen")
        self.chrome_options.add_argument("--headless")
        self.user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.137 Safari/537.36'
        self.chrome_options.add_argument(f'user-agent={self.user_agent}')
        self.chrome_options.add_argument("--no-sandbox")
        self.save_dir = self.output['market_ismi'].replace(' ', '_')
        self.create_save_dir()

    def fetch_discount_brochures(self):
        pass

    def bypass_cookie_popup(self, button_xpath):
        # Locate and click the cookie acceptance button using XPath
        cookie_button = self.driver.find_element(By.XPATH, button_xpath)
        try:
            cookie_button.click()
            print("Cookie popup bypassed successfully.")
            time.sleep(1)
        except Exception as e:
            print(f"No cookie popup or unable to find the cookie button. Error: {e}")

    def fix_month_name(self, input_month):
        valid_months = ['Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran', 'Temmuz', 'Ağustos',
                        'Eylül', 'Ekim', 'Kasım', 'Aralık']
        # Find the closest match from the list of valid months
        closest_match = difflib.get_close_matches(input_month.lower(), valid_months, n=1, cutoff=0.6)
        if closest_match:
            return closest_match[0]  # Return the best match
        else:
            return input_month

    def create_save_dir(self):
        os.makedirs(self.save_dir, exist_ok=True)

    def save_as_pdf(self, url_list, save_folder):
        images = []
        save_path = f"{os.path.join(save_folder, str(uuid4()))}.pdf"
        for url in url_list:
            try:
                # Fetch the image
                response = requests.get(url)
                response.raise_for_status()  # Raise an error if the request failed
                if '.pdf' in url:
                    with open(save_path, "wb") as f:
                        f.write(response.content)
                    return save_path
                # Open the image
                img = Image.open(BytesIO(response.content))
                # Convert to RGB if the image is in a different mode (e.g., RGBA or P)
                if img.mode != 'RGB':
                    img = img.convert('RGB')

                images.append(img)
            except Exception as e:
                print(f"Failed to process {url}: {e}")

        if images:
            images[0].save(save_path, save_all=True, append_images=images[1:])

            return save_path
        else:
            return ""
