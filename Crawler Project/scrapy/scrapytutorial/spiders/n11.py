import scrapy
from ..items import PriceCompareItem

class nonbir(scrapy.Spider):
    name = "n11"
    start_urls = ['https://www.n11.com/telefon-ve-aksesuarlari/cep-telefonu?m=Apple']
    allowed_domains = ['www.n11.com']
    page_number=2
    fieldname_counter=0

    def parse(self, response):
        item = PriceCompareItem()
        pageNumber = 20

        title = response.xpath("//*[@class='productName ']/text()").extract()
        price = response.xpath("//*[@class='productDisplayPrice']/@value").extract()
        link = response.xpath("//*[@class='pro']/a/@href").extract()
        
        for i in range(len(price)):
            price[i] = price[i].replace(',','')
        
        item['title'] = title
        item['price'] = price
        item['link'] = link
        item['market'] = 'N11'
        item['store'] = 'N11'
        yield item

        next_page = "https://www.n11.com/telefon-ve-aksesuarlari/cep-telefonu?m=Apple&pg={}".format(self.page_number)

        if next_page and self.page_number < pageNumber:
            self.page_number +=1
            yield response.follow(next_page, callback=self.parse)