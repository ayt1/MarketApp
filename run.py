from markets import *
from market_config import config
import json
from huey import MemoryHuey, crontab, RedisHuey
import os

huey = MemoryHuey()

@huey.periodic_task(crontab(minute='0', hour='7,23'))
def get_all_discounts():
    if os.path.exists("discounts.json"):
        with open("/home/aytac/market/discounts.json", "r", encoding='utf-8') as f:
            discount_data = json.load(f)
    else:
        discount_data = [val['output_json'] for val in config.values()]

    for (class_name, value), prev_data in zip(config.items(), discount_data):
        market = globals()[class_name](value)
        discount = market.fetch_discount_brochures()
        if discount['indirimler']:
            prev_data['indirimler'] = discount['indirimler']

    with open("discounts.json", "w") as f:
        json.dump(discount_data, f, indent=4, ensure_ascii=False)
