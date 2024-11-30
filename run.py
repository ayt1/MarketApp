from markets import *
from market_config import config
import json


discounts = []

# a101 = A101(config['a101'])
# bim = BIM(config['bim'])
# happy = HappyCenter(config['happy'])
# watsons = Watsons(config['watsons'])
# sok = Sok(config['sok'])
# onur = Onur(config['onur'])
#
# for market in [a101, bim, happy, watsons, sok, onur]:
#     markets.append(market.fetch_discount_brochures())

for value in config.values():
    market = value['class'](value)
    discounts.append(market.fetch_discount_brochures())

with open("discounts.json", "w") as f:
    json.dump(discounts, f, indent=4, ensure_ascii=False)
