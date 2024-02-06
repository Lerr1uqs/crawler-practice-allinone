from bs4 import BeautifulSoup
import requests
import pdb
import pandas as pd
from rich.progress import track
from selenium import webdriver

URL = "https://quote.eastmoney.com/SZ002743.html"
headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
}

chrome = webdriver.Chrome()
chrome.get(URL)

# content = requests.get(URL, headers=headers).text
# print(content)
soup = BeautifulSoup(chrome.page_source, "html.parser")
# 在网页里右键检查可以看到
table = soup.find("div", attrs={"class" : "finance4 afinance4"})
# assert len(table) == 1
# table = table[0]
print(table)

# Extract column headers
headers = [th.text.strip() for th in table.find('thead').find('tr').find_all('th')[1:]]

# Extract table rows
rows = []
name = [] # 名字+行业+行业排名+四分卫
attr = {
    "name":"", 
    "industry":"", 
    "rank":""
}
for idx, row in enumerate(table.find('tbody').find_all('tr')[:-1]): # 跳过最后一个四分位属性
    tds = row.find_all('td')

    if idx == 0:
        attr["name"] = tds[0].find("a").string.strip()

    elif idx == 1:
        attr["industry"] = \
            tds[0].find("div", attrs={"class":"hypj_hy"}) \
                  .find("a") \
                  .string \
                  .strip()
                  
    elif idx == 2:
        attr["rank"] = tds[0].string.strip()
        
    else:
        raise RuntimeError

    row_data = [td.text.strip().replace("亿", "y").replace("万", "w") for td in tds[1:]]
    print(row_data)
    rows.append(row_data)

# Create a DataFrame
headers = [
    "MC",  # market cap
    "NAV", 
    "NP", 
    "PE", 
    "PB", 
    "GPM", # Gross Profit Margin 
    "NPM", # Net Profit Margin
    "ROE"
]
df = pd.DataFrame(rows, columns=headers)

# Display the DataFrame
print(df)