import scrapy
from ..items import PriceCompareItem
import pdb

class Teknosa(scrapy.Spider):
    name = "teknosa"
    start_urls = ['https://www.teknosa.com/iphone-ios-telefonlar-c-100001001']
    allowed_domains = ['www.teknosa.com']
    page_number=2
    fieldname_counter=0

    def parse(self, response):

        item = PriceCompareItem()

        title = response.xpath("//*[@class='product-name']/a/span/text()").extract()
        price = response.xpath("//*[@class='product-price']/span/text()").extract()
        link =  response.xpath("//*[@class='product-name']/a/@href").extract()

        for i in range(len(price)):
            price[i] = price[i].replace('.','').replace('TL','').strip()
            link[i] = 'https://www.teknosa.com/' + link[i]

        item['title'] = title
        item['price'] = price
        item['link'] = link
        item['market'] = 'TEKNOSA'
        item['store'] = 'TEKNOSA'
        yield item

        next_page = "https://www.teknosa.com/iphone-ios-telefonlar-c-100001001?s=%3Arelevance&page={}".format(self.page_number)

        if next_page and self.page_number < 3:
            self.page_number +=1
            yield response.follow(next_page, callback=self.parse)



