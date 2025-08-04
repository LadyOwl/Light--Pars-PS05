import scrapy


class LightnewscrSpider(scrapy.Spider):
    name = "lightnewscr"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        lights = response.css("div.LlPhw")
        for light in lights:
            yield {
                "name": light.css("div.WdR1o span::text").get(),
                "price": light.css('div.ui-LD-ZU KIkOH span::text').get(),
                "url": light.css('a').attrib['href']

            }


