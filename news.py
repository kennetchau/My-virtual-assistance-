#A general get news function using BeautifulSoup to scrap news
import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen




def main(url):
    news_url = url
    Client = urlopen(news_url)
    xml_page = Client.read()
    Client.close()

    soup_page = soup(xml_page, "xml")
    news_list = soup_page.findAll("item")
    for news in news_list:
        print(news.title.text)
        print(news.link.text)
        print(news.pubDate.text)
        print("-"*10)