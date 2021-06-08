# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AnnamayaItem(scrapy.Item):
    # define the fields for your item here like:
    food_name = scrapy.Field()
    food_price = scrapy.Field()


pass
