import requests
import re
import csv


header = {'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0"}

obj = re.compile(
    r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>.*?'
                 r'<span class="rating_num" property="v:average">(?P<rating>.*?)</span>',
                 re.S)


file_name = 'douban.csv'
with open(file_name, mode = "w", encoding = 'utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['序号', '名称', '评分'])

    counter = 1

    for i in range(0, 251, 25):

        url = f"https://movie.douban.com/top250?start={i}&filter="

        resp = requests.get(url, headers=header)

        page_content = resp.text

        res = obj.finditer(page_content)

        for match in res:
            writer.writerow([counter, match.group('name'), match.group('rating')])
            counter += 1