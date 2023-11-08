
from bs4 import BeautifulSoup 
import requests
import urllib.request 
# import logging

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; win64;x64) Applewebkit/537.36(khtml,likegecko) Chrom/58.03029.110 Safari/537.3'
}

source = requests.get("https://www.freeimages.com/search/dog", headers=headers).text
soup = BeautifulSoup(source, "lxml")
#1st pip install lxml

Images = []
img_links=soup.select("img[src^='https://images.freeimages.com/images']")
# print(img_links)

for i in range(len(img_links)):
    Images.append(img_links[i]["src"])

# print(Images)
for i in range(len(Images)):
    name="D:\Datascience\dogImages"+str(i)+".jpg"
    urllib.request.urlretrieve(Images[i],name)
    