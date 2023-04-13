import scrapy
from ..items import PriceCompareItem


class VatanBilgisayar(scrapy.Spider):
    name = "vatan"
    start_urls = ['https://www.vatanbilgisayar.com/apple/cep-telefonu-modelleri']
    allowed_domains = ['www.vatanbilgisayar.com']
    page_number=2
    fieldname_counter=0

    def parse(self, response):


        item = PriceCompareItem()

        title = response.xpath("//*[@class='product-list__content']/a/div[2]/text()").extract()
        price = response.xpath("//*[@class='product-list__price']/text()").extract()
        link = response.xpath("//*[@class='product-list__content']/a/@href").extract()

        for i in range(len(title)):
            title[i] = title[i].replace(';','').strip()
            price[i] = price[i].replace('.','').strip()

        item['title'] = title
        item['price'] = price
        item['link'] = link
        item['market'] = 'VATAN'
        item['store'] = 'VATAN'
        yield item


        next_page = "https://www.vatanbilgisayar.com/apple/cep-telefonu-modelleri/?page={}".format(self.page_number)

        if next_page and self.page_number < 4:
            self.page_number +=1
            yield response.follow(next_page, callback=self.parse)



