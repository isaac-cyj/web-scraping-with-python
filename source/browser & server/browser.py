import requests
# Set the target webpage
url = "https://coinmarketcap.com/"
#custom headers
headers = {
    'User-Agent': 'Mobile'
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
with open("browser.html","w+",encoding='utf8') as w:
    w.write(str(response.text))