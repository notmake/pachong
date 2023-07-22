# 网站https://ssr1.scrape.center/  爬取首页10部电影的数据，然后将相关数据存储为TXT文本格式
import requests
from pyquery import PyQuery as pq
import re

url = 'https://ssr1.scrape.center'
html = requests.get(url).text
doc = pq(html)
items = doc('.el-card').items()

file = open('4.1movies.text', 'w', encoding='utf-8')
for item in items:
    # 电影名称
    name = item.find('a> h2').text()
    file.write(f'名称:{name}\n')
    # 类别
    categories = [item.text() for item in item.find('.categories button span').items()]
    file.write(f'类别:{categories}\n')
    # 上映时间
    shijian = item.find('.info:contains(上映)').text()
    shijian = re.search('(\\d{4}-\\d{2}-\\d{2})', shijian).group(1) \
    if shijian and re.search('(\\d{4}-\\d{2}-\\d{2})', shijian).group(1) else None
    file.write(f'上映时间:{shijian}\n')
    # 评分
    score = item.find('p.score').text()
    file.write(f'评分:{score}\n')



