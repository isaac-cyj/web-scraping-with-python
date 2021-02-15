import scrapy


class StraitstimeSpider(scrapy.Spider):
    name = 'straitstime'
    url = "https://www.straitstimes.com/"
    allowed_domains = [url]
    start_urls = [url]

    def parse(self, response):
        print('\n' * 10)

        for x in response.xpath('//img/@src').getall():
            print('\n' * 3)
            # returns img link dictionary
            yield {'Image Link': x}

