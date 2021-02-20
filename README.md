# web-scraping-with-python
This repo contains a spider which will be used to extract current Covid-19 data in Singapore. <br />
Browser is used to check the status code and response header of the targeted URL. You may specify a custom user-agent if you wish to.<br />
Server is a simple webserver which uses the sockets library. <br />

## Usage
#### Ensure that you are in the respective directory before running
>source\scripts\activate


## Spider 
>python -m scrapy runspider moh_covid19.py -o out.json

## Browser
>python browser.py -H https://moh.gov.sg/covid19 -ua Mobile -o browser.html

## Server
>python server.py 
