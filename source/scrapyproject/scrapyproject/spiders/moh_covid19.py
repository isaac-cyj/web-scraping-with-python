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
        doscornlevel = response.css('div.sfContentBlock span::text ').getall()[2]
        yield {"DOSCORN Level" : doscornlevel}

########################  retrieve last update  ########################
        lastupdate = response.css('div.sfContentBlock ::text ').getall()[20]
        lastupdate = lastupdate.replace(u'\u00a0', u' ')
        yield{"updated since" : lastupdate}

######################## return amount of imported cases ########################
        #remove \xa0 from the string
        importedcases  = response.css('div.sfContentBlock ::text ').getall()[22]
        importedcases = importedcases.replace(u'\xa0', u'')
        yield {"Amount of imported cases" : importedcases}







        #return image link
        #for x in MohCovid19Spider.images:
            #i += 1
            #print("image link %d"%(i))
            #yield {"image link %d"%(i): MohCovid19Spider.images["image link %d"%(i)]}


        for x in response.xpath('//img/@src').getall():
            yield {"image link": x}