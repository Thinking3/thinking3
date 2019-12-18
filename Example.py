import requests
import time
import re

url = "http"

b = requests.get(url).text
currentTime = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

pattern_reposts_count = re.compile('"reposts_count": ([0-9]*)')
pattern_comments_count = re.compile('"comments_count": ([0-9]*)')
pattern_attitudes_count = re.compile('"attitudes_count": ([0-9]*)')

# with open(name, 'w', encoding='utf-8') as f:
with open('/usr/share/nginx/html/data/xxx.csv', 'a') as f:
# match data
    reposts_count = re.findall(pattern_reposts_count, b)[0]
    comments_count = re.findall(pattern_comments_count, b)[0]
    attitudes_account = re.findall(pattern_attitudes_count, b)[0]
    f.writelines(currentTime + ',' + reposts_count + ',' + comments_count + ',' + attitudes_account + '\n')
    # f.write(b) 
    f.close()


