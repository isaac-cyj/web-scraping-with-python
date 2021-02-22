import scrapy

class MohCovid19Spider(scrapy.Spider):
    name = 'moh_covid19'
    #start_urls = [url]
    def start_requests(self):
        url = "https://www.moh.gov.sg/covid-19"
                                     #sends emtpy session cookie to request for new session
        yield scrapy.Request(url=url, cookies={'ASP.NET_SessionId': ''},callback=self.parse)

    def parse(self, response):
        #DOSCORN Level
        yield {'DOSCORN Level' : response.css('div.sfContentBlock h4 ::text').getall()[2]}

        #total number of imported cases in Singapore since x
        importedcases = response.css('div.sfContentBlock h3 strong ::text').getall()[1]
        importedcases = importedcases.replace(u'\u00a0', u' ')
        yield {'Imported Cases' : importedcases}
        #total number of imported cases in Singapore
        Timportedcases = response.css('div.sfContentBlock tr strong  ::text').getall()[4]
        Timportedcases = Timportedcases.replace(u'\u00a0', u'')
        yield {'Total Imported cases' : Timportedcases}
        #total number of imported cases in Singapore *increased by*
        Timportedcasesby = response.css('div.sfContentBlock tr strong  ::text').getall()[5]
        Timportedcasesby = Timportedcasesby.replace(u'+', u'')
        yield {'Imported cases increased by' : Timportedcasesby}


        #case summary in Singapore as of x
        yield {'Case summary' : response.css('div.sfContentBlock h3 strong ::text').getall()[2]}
        #Active cases
        yield {'Active cases' : response.css('div.sfContentBlock tr span b ::text').getall()[0]}
        #Discharged
        yield {'Discharged' : response.css('div.sfContentBlock tr span b ::text').getall()[1]}
        #In Community Facilities
        yield {'In Community Facilities' : response.css('div.sfContentBlock tr span b ::text').getall()[2]}
        #Hospitalised (Stable)
        yield {'Hospitalised (Stable)' : response.css('div.sfContentBlock tr span b ::text').getall()[3]}
        #Hospitalised (Critical)
        yield {'Hospitalised (Critical)' : response.css('div.sfContentBlock tr span b ::text').getall()[4]}
        #Deaths
        yield {'Deaths' : response.css('div.sfContentBlock tr span b ::text').getall()[5]}


        #Number Of Swab Teseted as of x
        swabtested = response.css('div.sfContentBlock h3 strong ::text').getall()[3] + ' ' + response.css('div.sfContentBlock h3 strong ::text').getall()[4]
        swabtested = swabtested.replace(u'\u00a0', u'')
        yield{'Swab Tested' : swabtested}
        #Total Swab Tested
        yield {'Total Swab Tested' : response.css('div.sfContentBlock tr span b ::text').getall()[6]}
        #Average Daily Number Of Swabs Tested Over The Past Week
        Adailyswab = response.css('div.sfContentBlock td strong ::text').getall()[11]
        Adailyswab =  Adailyswab.replace(u'~', u'')
        yield {'Average Daily Swabs Tested Over The Past Week' : Adailyswab}
        #Total Swabs Per 1,000,000 Total Population
        Tswabsper1m = response.css('div.sfContentBlock td strong ::text').getall()[12]
        Tswabsper1m = Tswabsper1m.replace(u'~', u'')
        yield {'Total Swabs Per 1mil Total Population' : Tswabsper1m}


        #Latest Update
        latestupdate = response.css('div.sfContentBlock tr td ::text').getall()[30]
        latestupdate = latestupdate.replace(u'\u00a0', u'')
        yield {'Latest Update' : latestupdate}
        #Latest info
        yield {'Latest Info' : response.css('div.sfContentBlock tr td ::text').getall()[31]}


        #Get all image
        for x in response.xpath('//img/@src').getall():
            yield {"image link": x}
        print('\n'*5)
        print(response.request.headers['User-Agent'])
        ############ save output ############
        with open("moh_covid19.html", "w+", encoding='utf8') as w:
            w.write(str(response.text))

#example usage
#ensure cookies is enabled and cache is disabled
#python -m scrapy runspider moh_covid19.py -o out.json
