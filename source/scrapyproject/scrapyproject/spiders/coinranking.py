import scrapy

class CoinrankingSpider(scrapy.Spider):
    name = 'coinranking'
    allowed_domains = ['https://coinranking.com/']
    start_urls = ['https://coinranking.com/']

    def parse(self, response):
        # css selector selects HTML elements based on which HTML tag you specify
        # print(response.css('img'))
        print('\n' * 10)

        for x in response.xpath('//img/@src').getall():
            print(x)
            print('\n' * 3)

            # returns img link dictionary
            yield {'Image Link': x}


            Page_selector = '.next a ::attr(href)'
            next_page = response.css(Page_selector).extract_first()
            if next_page:
                print("next page")
                yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

    # scrapy runspider coinranking.py -o results.json -t json
    # scrapy shell https://coinranking.com/
    # using shell to handle response manually
    # response.css('img').xpath('@src').get() or response.css('img').xpath('@src').getall()

    # more about xpath
    # https://www.w3schools.com/xml/xpath_syntax.asphttps://www.w3schools.com/xml/xpath_syntax.asp
    # https://docs.scrapy.org/en/latest/topics/selectors.html
    # https://docs.scrapy.org/en/latest/_static/selectors-sample1.htmll