import scrapy


class LightnewscrSpider(scrapy.Spider):
    name = "lightnewscr"
    allowed_domains = ["https://hoff.ru"]
    start_urls = ["https://hoff.ru/catalog/tovary_dlya_doma/osveschenie/"]

    def parse(self, response):
        pass
