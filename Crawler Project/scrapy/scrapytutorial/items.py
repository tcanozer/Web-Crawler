# Define here the models for your scraped items

import scrapy
from scrapy.item import Field

class ScrapytutorialItem(scrapy.Item):
	# define the fields for your item here like:
	# name = scrapy.Field()
	
	# only one field that it of Quote.
	Quote = scrapy.Field()


class PriceCompareItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    link = scrapy.Field()
    store = scrapy.Field()
    market = scrapy.Field()
    pass