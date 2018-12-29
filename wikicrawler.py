import requests
from bs4 import BeautifulSoup
import re


pages=[]
pages2=[]
highPos=[]
found=False
sol=[]
banned=["/wiki/Wikipedia","/wiki/Special","/wiki/Help","/wiki/Category","/wiki/Portal"]


url1="/wiki/istanbul"
url2="/wiki/Middle_East_Technical_University"

def crawlByList(list):
    global found
    for e in list:
        if found==True:
            break
        print(e)
        crawl(e)


        list=[]

def crawlRecursively():
    global sol
    if len(sol)==0:
        return []
    else:
        crawl(sol[0])
        return crawlByList(sol[1:])



def crawl(url):
    global pages
    global found
    global url2
    global sol
    url = requests.get("https://en.wikipedia.org"+url)
    soup = BeautifulSoup(url.text,"html.parser")
    for link in soup.findAll("a",href=re.compile("^(/wiki/)")):
        if "href" in link.attrs:

            if link.attrs["href"] not in pages:
                page = link.attrs["href"]
                pages.append(page)
                if page==url2:
                    found=True
                    print("/////////////////////////////////////   "+page)
                    print("found")
                    return 1
                if page in pages2:
                    print("          "+page)
                    highPos.append(page)
    sol=highPos+pages


    return sol



def crawlBack(url):
    global pages2
    global banned
    url = requests.get("https://en.wikipedia.org"+url)
    soup = BeautifulSoup(url.text,"html.parser")
    for link in soup.findAll("a",href=re.compile("^(/wiki/)")):
        if "href" in link.attrs:

            if link.attrs["href"] not in pages:
                page = link.attrs["href"]
                if page.split(":")[0] not in banned:
                    pages2.append(page)


crawlBack(url2)
crawl(url1)
crawlRecursively()
