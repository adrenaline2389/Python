import re
import requests
from bs4 import BeautifulSoup

#
# pattern = r"hel.*?xxx"
# string = "helhelhelxxxhelhelxxx"
#
# match = re.match(pattern, string)
# if match:
#     print("匹配成功:", match.group())
# else:
#     print("匹配失败")

# 第一种 正则爬虫
url = r"https://movie.douban.com/top250?start=%3E{(page"
headers = {
    'user-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0'
}
# 访问网址
rep = requests.get(url, headers=headers)
print(rep)

# 匹配名称
title = re.compile( r'<li>.*?<span class="title">(?P<name>.*?)</span>', re.S)
result = title.finditer(rep.text)
print(result)
for it in result:
    print(it)
    print(it.group("name"))

# 匹配评分
score = re.compile( r'<li>.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>', re.S)
result = score.finditer(rep.text)
for it in result:
    print(it.group("score"))

#匹配名言
words = re.compile(r'<li>.*?<span class="inq">(?P<words>.*?)</span>', re.S)
result = words.finditer(rep.text)
for it in result:
    print(it.group("words"))


# 第二种 beautifulSoup4
url = r"https://movie.douban.com/top250?start=%3E{(page"
headers = {
    'user-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0'
}
# 访问网址
rep = requests.get(url, headers=headers)
soup = BeautifulSoup(rep.content, 'html.parser')

# 查找包含电影列表的<ol>标签
movies_list = soup.find('ol', class_='grid_view')
# print(soup)

# 遍历所有<li>标签，提取每部电影的信息
for li in movies_list.find_all('li'):
    # 提取电影标题
    title = li.find('span', class_='title').text
    # 提取电影评分
    rating = li.find('span', class_='rating_num').text
    # 提取评价人数
    # rating_people = li.find('span', text=lambda x: '人评价' in x).text
    # 提取一句话总结（如果存在）
    quote = li.find('span', class_='inq')
    quote_text = quote.text if quote else "暂无"

    # 输出结果
    print(f"电影名称: {title}")
    print(f"评分: {rating}")
    # print(f"评价人数: {rating_people}")
    print(f"一句话总结: {quote_text}")
    print("-" * 40)


# 第三种 lxml