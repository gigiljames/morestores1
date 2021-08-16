import scrapy
from ..items import Morestores1Item

class Morescrape1Spider(scrapy.Spider):
    name = 'morescrape1'
    allowed_domains = ['moreretail.in']
    start_urls = ['http://moreretail.in/']

    def start_requests(self):
        url = r'https://www.moreretail.in/api/store-api?city=&pincode=&market=&pagination_count=1000'
        yield scrapy.Request(url = url, callback=self.parse_page)

    def parse_page(self, response):
        rows = Morestores1Item()
        json_response = response.json()
        rows = json_response.get('data', {}).get('data', [])
        for row in rows:
            yield row
