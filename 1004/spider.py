import requests
import re

base_url = 'https://ssr1.scrape.center/'
fragments = []
# new_url = [[0 for _ in range(10)] for _ in range(10)]

for i in range(1, 11):
    url = f"https://ssr1.scrape.center/page/{i}"

    response = requests.get(url)

    code = response.text

    page = re.compile(
     r'<a data-v-7f856186="" href=".*?(?P<detail>.*?)" class="name">.*?',
    re.S)

    results = re.findall(page, code)


    for result in results:
        # fragments.append(result)
        url_detail = base_url+result
        detail_code = requests.get(url_detail).text
        names = re.findall(r'<h2 data-v-63864230="" class="m-b-sm">.*?(?P<name>.*?)</h2></a>.*?', detail_code, re.S)
        scores = re.findall(r'<p.*?score.*?>\n              .*?(?P<score>.*?)</p>.*?', detail_code, re.S)
        print(names + scores)

# for i in range(1, 11):
#     url = f"{base_url}/page/{i}"
#     for j in range(10):
#         new = url + fragments[j]
#         new_url[i - 1][j] = new
#
# rows = len(new_url)
# cols = len(new_url[0])
#
# for i in range(rows):
#     for j in range(cols):
#         url = new_url[i][j]
