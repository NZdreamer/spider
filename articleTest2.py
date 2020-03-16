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
        print("get HTML failed")

def getArticle(html):
    soup = BeautifulSoup(html,"html.parser")
    title = soup.find('h1','article-title') #title标签
    content = soup.find('article') #正文标签
    article = title.string + '\n\n\n'
    for p in content.children:
        if p.string != '\n':
            article = article + p.text + '\n\n'
    return article

def saveFile(article):   
    root = "F:/novels/"
    path = root + "new" + ".txt"
    if not os.path.exists(root):
        os.mkdir(root)
    with open(path, 'wt',encoding = 'utf-8') as f:
        f.write(article)
        print("文件保存成功")


def main():
    url = "https://www.zhenhunxiaoshuo.com/688.html"
    html = getHTMLText(url)
    article = getArticle(html)
    saveFile(article)

main()
