import scrapy

class blogspider(scrapy.Spider):
    name = "blog"
    allowed_domains = ["pramod.net"]
    start_urls = ["http://pramode.net/"]
    
    def parse(self, response):
        urls = response.xpath('//a/@href').extract()
        for url in urls:
            print url

            
