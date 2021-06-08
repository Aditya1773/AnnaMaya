from abc import ABC

import scrapy
from ..items import AnnamayaItem


class AnnaSpider(scrapy.Spider):
    name = 'Anna'
    start_urls = [
        'http://https://www.hyattrestaurants.com/en/dining/india/new-delhi/annamaya-restaurant-menu?utm_source=gmbAnnaMaya_DELAZ/'
    ]

    def parse(self, response):
        items = AnnamayaItem()
        food_name = response.css('i-name scala.mb-1::text').extract()
        food_price = response.css('.i-rate::text').extract()
        items['food_name'] = food_name
        items['food_price'] = food_price
        yield items
        pass
