import requests
import os
url = "https://www.nationalgeographic.com/content/dam/photography/photo-of-the-day/2020/01/pod-12-01-20.adapt.945.1.jpg"
root = "F:/tests/"
path = root + url.split("/")[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            #f.close()
            print("succeeded!")
    else:
        print("file already exist")
except:
    print("failed...")
