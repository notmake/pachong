import requests
import logging
import re
from urllib.parse import urljoin
import json
from os import makedirs
from os.path import exists
import multiprocessing

RESULTS_DIR = 'results'
exists(RESULTS_DIR) or makedirs(RESULTS_DIR)


def save_data(data):
    name = data.get('name')
    data_path = f'{RESULTS_DIR}/{name}.json'
    json.dump(data, open(data_path, 'w', encoding='utf-8'),
              ensure_ascii=False, indent=2)


""" 第一步 引库 request urllib的urljoin模板 re库 logging库用来输出信息   """
"""第二步：开始定义 最初 url必需的 """
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')
BASE_URL = 'https://ssr1.scrape.center'
TOTAL_PAGE = 10
"""
第三步开始爬取网页 

1.获取HTML代码
2.解析代码
3.保存数据
"""


# 先写一个通用的爬取页面的方法
def scrape_page(url):
    logging.info('scraping %s...', url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        logging.error('get invalid status code %s while scraping %s',
                      response.status_code, url)
    except requests.RequestException:
        logging.error('error occurred while scraping %s', url,
                      exc_info=True)


# 定义列表页
def liebiao_url(page):
    liebiaoye_url = f'{BASE_URL}/page/{page}'
    return scrape_page(liebiaoye_url)


# 开始解析
# 解析列表页 得到每部电影的详情页的URL
def xiangqing_url(html):
    pattern = re.compile('<a.*?href="(.*?)".*?class="name">')
    items = re.findall(pattern, html)
    for item in items:
        yangqingye_url = urljoin(BASE_URL, item)
        logging.info('get detail url %s', yangqingye_url)
        yield yangqingye_url


# 解析详情页


def scrap_detail(url):
    return scrape_page(url)


def xaingqingye_neirong(html):
    cover_pattern = re.compile('class="item.*?<img.*?src="(.*?)".*?class="cover">', re.S)
    name_pattern = re.compile('<h2.*?>(.*?)</h2>')
    categories_pattern = re.compile('<button.*?category.*?<span>(.*?)</span>.*?</button>', re.S)
    shijian_pattern = re.compile('(\\d{4}-\\d{2}-\\d{2})\\s?上映')
    drama_pattern = re.compile('<div.*?drama.*?>.*?<p.*?>(.*?)</p>', re.S)
    score_pattern = re.compile('<p.*?score.*?>(.*?)</p>', re.S)
    cover = re.search(cover_pattern, html).group(1).strip()
    name = re.search(name_pattern, html).group(1).strip()
    categories = re.search(categories_pattern, html).group(1).strip()
    shijian = re.search(shijian_pattern, html).group(1).strip()
    dram = re.search(drama_pattern, html).group(1).strip()
    score = re.search(score_pattern, html).group(1).strip()
    return {
        '封面': cover,
        '名字': name,
        '类别': categories,
        '上映时间': shijian,
        '评分': score,
        '内容': dram
    }




def main():
    for page in range(1, TOTAL_PAGE):
        index_html = liebiao_url(page)
        details_urls = xiangqing_url(index_html)
        for detail_url in details_urls:
            detail_html = scrap_detail(detail_url)
            data = xaingqingye_neirong(detail_html)
            logging.info('get datail data %s', data)
            logging.info('saving data to json file')
            save_data(data)
            logging.info('data saved successfully')


main()
















