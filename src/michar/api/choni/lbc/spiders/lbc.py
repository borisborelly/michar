import scrapy


class LbcSpider(scrapy.Spider):
    name = "lbc"
    allowed_domains = ["longbeach.legistar.com"]
    start_urls = ["https://longbeach.legistar.com/Calendar.aspx"]

    def parse(self, response):
        pass
