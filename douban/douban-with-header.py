import requests
headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
}

URL = "https://movie.douban.com/top250"
response = requests.get(URL, headers=headers)
print(response.text)
