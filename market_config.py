from markets import *

config = {
    "bim": {
        "main_url": "https://www.bim.com.tr/Categories/680/afisler.aspx",
        "output_json": {"market_ismi": "BIM",
                        "indirimler": [],
                        "logo_url": "https://www.bim.com.tr/Gorseller/Genel/B%C4%B0M%20LOGO.jpg"
                        },
        "class": BIM
    },
    "a101": {
        "main_url": "https://www.a101.com.tr",
        "output_json": {"market_ismi": "A101",
                        "indirimler": [],
                        "logo_url": "https://upload.wikimedia.org/wikipedia/commons/d/df/A101_logo.svg"
                        },
        "class": A101
    },
    "sok": {
        "main_url": "https://www.sokmarket.com.tr",
        "output_json": {"market_ismi": "ŞOK",
                        "indirimler": [],
                        "logo_url": "https://kurumsal.sokmarket.com.tr/Assets/images/logo/sokmarketler.png"
                        },
        "class": Sok
    },
    "happy": {
        "main_url": "https://www.happycenter.com.tr/kurumsal/indirim-bulteni/#sayfa",
        "output_json": {"market_ismi": "Happy Center",
                        "indirimler": [],
                        "logo_url": "https://static.happycenter.com.tr/Uploads/Kurumsal/logo-046DB-300x0.png"
                        },
        "class": HappyCenter
    },
    "watsons": {
        "main_url": "https://katalog.watsons.com.tr/",
        "output_json": {"market_ismi": "Watsons",
                        "indirimler": [],
                        "logo_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Watsons_logotype.svg/1200px-Watsons_logotype.svg.png"
                        },
        "class": Watsons
    },
    "onur": {
        "main_url": "https://www.onurmarket.com/kataloglar",
        "output_json": {"market_ismi": "Onur Market",
                        "indirimler": [],
                        "logo_url": "https://kurumsal.onurmarket.com/pics/news/9_2_guncel-logo-kullanimimiz.jpg"
                        },
        "class": Onur
    },
    # "gratis": {
    #     "main_url": "https://www.gratis.com/kampanyalar",
    #     "output_json": {"market_ismi": "Gratis",
    #                     "indirimler": [],
    #                     "logo_url": "https://www.evrensel.net/upload/dosya/158520.jpg"
    #                     }
    # }
}