import urllib.request
import requests
from bs4 import BeautifulSoup as bsf


class news():
    def __init__(self):
        self.__newsList=[]
        page = requests.get("https://timesofindia.indiatimes.com/coronavirus/")
        src = page.content

        soup = bsf(src,"html.parser")
        li=[]
        li2=[]
        target_division = soup.findAll("div",{"class":"news-list"})
        for i in target_division:
            x = i.findAll("div",{"class":"Ze-gt"})
            # print("z")
            li.extend(x)
        for i in li:
            x = i.find("div",{"class":"row-news-list"})
            if x is not None:
                li2.extend(x)
        li=[]
        sub_li=[]
        count =0
        for i in li2:
            dictr={}
            dictr[i.get_text()] = i["href"]
            self.__newsList.append(dictr)


    def get_news(self,count=None):
        subli=[]
        if count == None:
            return self.__newsList
        else:
            return self.__newsList[:count]


# x = news()
# li = x.get_news(4)
# f = open("abc.txt","w")
# for i in li:
#     f.write(str(i))
#     f.write("\n")