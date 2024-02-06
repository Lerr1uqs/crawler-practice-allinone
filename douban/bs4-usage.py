from bs4 import BeautifulSoup
import requests
import pdb

URL = "http://books.toscrape.com/"

content = requests.get(URL).text
soup = BeautifulSoup(content, "html.parser")
pdb.set_trace()
prices = soup.findAll("p", attrs={"class", "price_color"})
for price in prices:
    print(price)

# 这里可以打印price.string 得到中间的东西
'''
<p class="price_color">Â£51.77</p>
<p class="price_color">Â£53.74</p>
<p class="price_color">Â£50.10</p>
<p class="price_color">Â£47.82</p>
<p class="price_color">Â£54.23</p>
'''

