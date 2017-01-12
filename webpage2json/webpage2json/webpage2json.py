import requests    
from bs4 import BeautifulSoup

r = requests.get("http://www.ebizmba.com/articles/torrent-websites")

soup = BeautifulSoup(r.text, "html.parser")
data = soup.find_all("div", {"class:", "main-container-2"})

for i in data:
    for j in i.contents[1].find_all("a"):
        print(j.get('href'))