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


        yield {"DOSCORN Level" : response.css('div.sfContentBlock tr  ::text').getall()[7]}

        lastupdate = response.css('div.sfContentBlock ::text ').getall()[20]
        lastupdate = lastupdate.replace(u'\xa0', u' ')
        yield{"case updated since" : lastupdate}

        importedcases  = response.css('div.sfContentBlock tr  ::text').getall()[11]
        importedcases = importedcases.replace(u'\xa0', u'')
        yield {"Amount of imported cases" : importedcases}

        yield{"summary" : response.css('div.sfContentBlock ::text').getall()[26]}
        yield {"Active Cases" : response.css('div.sfContentBlock tr  ::text').getall()[16]}
        yield {"Discharged" : response.css('div.sfContentBlock tr  ::text').getall()[18]}
        yield {"In community facilities" : response.css('div.sfContentBlock tr  ::text').getall()[20] }
        yield {"Hospitalised (Stable)" : response.css('div.sfContentBlock tr  ::text').getall()[22]}
        yield {"Hospitalised (Crictal)" : response.css('div.sfContentBlock tr  ::text').getall()[24]}
        yield {"Deaths" : response.css('div.sfContentBlock tr  ::text').getall()[27]}

        swabtested = response.css('div.sfContentBlock ::text').getall()[57] +  response.css('div.sfContentBlock ::text').getall()[58]
        swabtested = swabtested.replace(u'\u00a0',u'')
        yield {"swab tested since " : swabtested}

        yield {"Total swab tested" : response.css('div.sfContentBlock tr  ::text').getall()[28]}
        yield{"Average Daily Number Of Swabs Tested Over The Past Week":response.css('div.sfContentBlock tr  ::text').getall()[29]}
        yield{"Total Swabs Per 1,000,000 Total Population":response.css('div.sfContentBlock tr  ::text').getall()[30]}







        #return image link
        #for x in MohCovid19Spider.images:
            #i += 1
            #print("image link %d"%(i))
            #yield {"image link %d"%(i): MohCovid19Spider.images["image link %d"%(i)]}


        for x in response.xpath('//img/@src').getall():
            yield {"image link": x}