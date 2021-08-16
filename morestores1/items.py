# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Morestores1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    city = scrapy.Field()
    state = scrapy.Field()
    address = scrapy.Field()
    pincode = scrapy.Field()
    contact = scrapy.Field()
    store_type = scrapy.Field()
    weekdays_timing = scrapy.Field()
    map_location = scrapy.Field()