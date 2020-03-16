import requests
from bs4 import BeautifulSoup
import os

def getHTMLText(url):
    myheaders = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}               
    try:
        r = requests.get(url, headers = myheaders, timeout = 30)
        r.raise_for_status()
        r.encoding = r. apparent_encoding
        return r.text
    except:
        return "get HTML failed"

def saveArticle(html):
    soup = BeautifulSoup(html,"html.parser")
    title = soup.find('h1','article-title') #title标签
    content = soup.find('article') #正文标签
    
    root = "F:/novels/"
    path = root + title.string + ".txt"
    if not os.path.exists(root):
        os.mkdir(root)
    with open(path, 'wt') as f:
        f.write(title.string + '\n\n')
        for p in content.children:
            if p.string != '\n':
                f.write(p.string + '\n\n')
        print("文件保存成功")


def main():
    url = "https://www.zhenhunxiaoshuo.com/688.html"
    html = getHTMLText(url)
    saveArticle(html)

main()
