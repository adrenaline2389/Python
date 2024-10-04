import requests
import re

url = 'https://www.hkogo.com/html/104084/36186464.html'
header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0'}

obj = re.compile(
    r'<div class="content" id="content">(.*?) <div style="display:none;">', re.S)

resp = requests.get(url, headers=header)

page_content = resp.text

res = obj.finditer(page_content)

for match in res:
    chapter = match.group(1)
    p_tags = re.findall(r'<p>(.*?)</p>', chapter, re.S)
    for i in p_tags:
        print(i)