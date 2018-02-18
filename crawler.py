from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import urllib.request


# test url
#https://www.youtube.co.uk/results?search_query=demons+imagine
final_name = []
final_url = []
def crawl(name, results):
    detail_urls = []
    formatted = name.lower().replace(" ", "+")
    url = 'https://www.youtube.co.uk/results?search_query=' + str(formatted)

    # opening theurl
    html = urlopen(url)
    soup = bs(html, 'lxml')
    links = list(soup.findAll("a"))
    test_link = len('/watch?v=IhP3J0j9JmY')

    for l in links:
        # appending the links that are videos and that are not already in the list
        if (len(l["href"])) == test_link and "https://www.youtube.com" + str(l["href"]) not in detail_urls:
            a = ("https://www.youtube.com" + str(l["href"]))
            detail_urls.append(a)
        else:
            pass
    # get the title of each video
    x = 0
    for u in (detail_urls):

        # try crawling each pages
        html = urlopen(u)
        sp = bs(html, 'lxml')
        # content = sp.find("span", {"class":"title" ,"dir":"ltr"})
        try:
            content = sp.find("span", {"class":"watch-title", "id":"eow-title"})
            fin = content.get_text().replace("\n", "")
            final_name.append(fin)
            final_url.append(u)
            x += 1
        except:
            pass
        
        if x == results:
            break
