# import scrapy
# from tutorial.items import DmozItem
#

from scrapy.spiders import Spider
from scrapy.selector import Selector

from tutorial.items import DmozItem


class DmozSpider(Spider):
    name = "baidu"
    allowed_domains = ["baidu.com"]
    start_urls = [
        "http://news.baidu.com/"
    ]

    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html
        @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
        @scrapes name
        """
        sites = response.css('#site-list-content > div.site-item > div.title-and-desc')
        items = []

        for site in sites:
            item = DmozItem()
            item['name'] = site.css(
                'a > div.site-title::text').extract_first().strip()
            item['url'] = site.xpath(
                'a/@href').extract_first().strip()
            item['description'] = site.css(
                'div.site-descr::text').extract_first().strip()
            items.append(item)

        return items
