from bs4 import BeautifulSoup
import requests
import sys

sys.path.append("..")
from utile.Threader import threader  # noqa
from utile.Timer import timer  # noqa


def url_finder():
    res = requests.request("GET", url='https://www.fullstackpython.com/blog.html')
    soup = BeautifulSoup(res.content, 'html5lib')
    links = soup.find_all('div', attrs={'class': 'c12'})[1]
    links = links.find_all('div', attrs={'class': 'row'})
    url_list = list()
    for link in links:
        url_list.append(['https://www.fullstackpython.com' + link.find('a')['href']])
    return url_list


def scrape_blog(link):
    response = requests.request("GET", url=link)
    soup = BeautifulSoup(response.content, 'html5lib')
    if soup.find('div', attrs={'class': 'c9'}) is None:
        return None
    else:
        blog = [str(i.text) for i in soup.find('div', attrs={'class': 'c9'}).find_all(['p', 'pre'])]
    return "".join(blog)


@timer()
@threader({scrape_blog: url_finder()})
def base():
    pass


print(base())
