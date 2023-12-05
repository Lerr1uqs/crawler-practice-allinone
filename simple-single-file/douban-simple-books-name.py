'''
author: Ler2sq
Data: 2023-12-5
'''
import requests
import unittest
import re

def get():
    url = "https://movie.douban.com/chart"
    # f12 -> 网络 -> chart -> 标头
    headers = {'User-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"}
    response = requests.get(url, headers=headers)
    return response

class CrawlerUT(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.response = get()
        
    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)
    
    def test_re_match(self):
        # f12 -> 网络 -> chart -> 响应
        # <a class="nbg" href="https://movie.douban.com/subject/10810266/"  title="93国际列车大劫案：莫斯科行动">
        # 这里的 .*? 是任意匹配的 non-greedy 模式 而.*是greedy-match
        pattern = re.compile('<a class=.*? href=.*?title="(.*?)">')
        items = re.findall(pattern, self.response.text)
        # print(items)
        self.assertEqual(items,
            ['93国际列车大劫案：莫斯科行动', 
             '杀手', 
             '坠落的审判', 
             'AI创世者', 
             '照明商店', 
             '名侦探柯南：黑铁的鱼影', 
             '进击的巨人 最终季 完结篇 后篇', 
             '不虚此行', 
             '猜谜女士', 
             '奥本海默']
        )


if __name__ == "__main__":
    unittest.main()