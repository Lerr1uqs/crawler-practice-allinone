from bs4 import BeautifulSoup
import requests
import pdb
from rich.progress import track

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
}
URL = "https://movie.douban.com/top250?start={}&filter="

top250 = []

for start_nr in track(range(0, 251, 25), description="crawling"):

    content = requests.get(URL.format(start_nr), headers=headers).text
    # print(content)
    soup = BeautifulSoup(content, "html.parser")
    # 在网页里右键检查可以看到
    titles = soup.find_all("span", attrs={"class" : "title"})
    
    for title in titles:
        # 这里会找出来一个原版标题
        if '/' in title.string:
            continue
        # print(title.string)
        top250.append(title.string)

print(top250)
print(len(top250))