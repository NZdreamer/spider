import requests
from bs4 import BeautifulSoup
import os



# 由网页url链接得到网页的html
def getHTMLText(url):
    myheaders = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}               
    try:
        r = requests.get(url, headers = myheaders, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("连接错误")

# 传入网页html，返回正文内容
def getArticle(html):
    soup = BeautifulSoup(html, "html.parser")
    title = soup.find(class_ = 'article-title') # title标签
    content = soup.find('article')  # 正文标签
    article = title.string + '\n\n'
    for p in content.children:
        if p.string != '\n':    # 过滤p标签间的换行符
            article = article + p.text + '\n\n' # p.text过滤非文本信息
    article = article + '\f'
    return article

# 返回书名
def getBookName(html):
    soup = BeautifulSoup(html, "html.parser")
    name = soup.find(class_ = 'focusbox-title').string
    return name

# 传入目录网页html，返回所有章节url列表
def getCharpterUrls(html):
    soup = BeautifulSoup(html, "html.parser")
    urlList = []
    for link in soup.find_all('article'):
        urlList.append(link.a.attrs['href']) # link.a.get('href')
    return urlList

# 小说内容写入txt文件
def saveToFile(name, charpters):
    root = "F:/novels/"
    path = root + name + ".txt" 
    if not os.path.exists(root):
        os.mkdir(root)
    f = open(path, 'wt', encoding = 'utf-8')    # 否则有编码问题
    print("------开始下载------")
    for charpter in charpters:
        charpterHtml = getHTMLText(charpter)
        article = getArticle(charpterHtml)
        f.write(article)
    f.close()
    print("《" + name + "》下载成功！")


def main():
    url = "http://www."  # 改url链接
    html = getHTMLText(url)
    bookName = getBookName(html)
    charpterUrls = getCharpterUrls(html)
    saveToFile(bookName, charpterUrls)

main()

    
