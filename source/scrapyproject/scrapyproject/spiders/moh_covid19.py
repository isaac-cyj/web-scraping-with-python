import scrapy


class MohCovid19Spider(scrapy.Spider):
    name = 'moh_covid19'
    url = "https://www.moh.gov.sg/covid-19"
    allowed_domains = [url]
    start_urls = [url]

    #class attributes
    #images = {}

    def parse(self, response):
        print('\n' * 10)
        print(response.url)

      #  i = 0
        #get images
      #  for x in response.xpath('//img/@src').getall():
            # returns img link dictionary
         #   i+=1
           # MohCovid19Spider.images["image link %d"%(i)] = x
       # i = 0


########################  return DOSCORN Level ########################
        yield {"DOSCORN Level" : response.css('div.sfContentBlock tr  ::text').getall()[7]}

########################  retrieve last update  ########################
        lastupdate = response.css('div.sfContentBlock ::text ').getall()[20]
        lastupdate = lastupdate.replace(u'\xa0', u' ')
        yield{"updated since" : lastupdate}

######################## return amount of imported cases ########################
        #remove \xa0 from the string
        importedcases  = response.css('div.sfContentBlock tr  ::text').getall()[11]
        importedcases = importedcases.replace(u'\xa0', u'')
        yield {"Amount of imported cases" : importedcases}

        yield{"summary" : response.css('div.sfContentBlock ::text').getall()[26]}
        yield {"Active Cases" : response.css('div.sfContentBlock tr  ::text').getall()[16]}
        yield {"Discharged" : response.css('div.sfContentBlock tr  ::text').getall()[18]}






        #return image link
        #for x in MohCovid19Spider.images:
            #i += 1
            #print("image link %d"%(i))
            #yield {"image link %d"%(i): MohCovid19Spider.images["image link %d"%(i)]}


        for x in response.xpath('//img/@src').getall():
            yield {"image link": x}