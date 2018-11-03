import scrapy

class CarsinfoSpider(scrapy.Spider):
    name = 'carsinfo'
    allowed_domains = ['https://www.zigwheels.com/launches']
    start_urls = ['https://www.zigwheels.com/launches/']
    
     
    def parse(self, response):
        titles =  response.xpath('//h3[@class="ml-0 fnt-18-d pt-0"]/text()').extract()
        prices =  response.xpath('//p[@class="fnt-18 zw-cmn-price b"]/text()').extract()
        carslist = zip(titles,prices)
        for item in carslist:
            yield {'title':item[0], 'price':item[1]}
