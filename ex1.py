import requests
url ="https://item.jd.com/100004770263.html"
try:
    r = requests.get(url,timeout=30)
    #r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
except:
    print("exception")
