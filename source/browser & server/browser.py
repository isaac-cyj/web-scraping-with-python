import requests
import argparse

def browser(url,filename,useragent):
    #custom headers
    headers = {
        'User-Agent': useragent
    }

    ###################### perform a "get" request on the target url ######################
    response = requests.get(url, headers=headers)
    print(f"\n{url} status code: %s" %(response.status_code))
    if (response.status_code == 200):
        print("OK\n")
    #print website source code
    #print(response.text)

    # This will just get just the headers
    h = requests.head(url,headers=headers)
    print(f"{url} response header:")
    for x in h.headers:
        print("\t ", x, ":", h.headers[x])

    print("*"*100)
    ######################  test what headers are sent by sending a request to HTTPBin ######################
    url2 = 'https://httpbin.org/headers'
    sentheaders = requests.get(url2, headers=headers)
    #check if modified header is correct
    print(f"\nHeaders sent to  {url2} and {url} %s\t " %(sentheaders.text))


    ############ save output ############
    with open(filename,"w+",encoding='utf8') as w:
        w.write(str(response.text))


#-h help
parser = argparse.ArgumentParser(description="This script displays target website status and header")
parser.add_argument("-H", "--host", required=True, help="specify the hostname or website name eg. http://foo.com:8080")
parser.add_argument("-o", "--out",type=str,help="save the page source, eg. browser.html [open output with firefox for best result]")
parser.add_argument("-ua","--useragent",type=str,default="python user-agent",help="specify custom user-agent, eg. Mobile")

args = parser.parse_args();
browser(args.host, args.out,args.useragent);

#example usage browser.py -H https://www.straitstimes.com:443  -ua Mobile -o out.html