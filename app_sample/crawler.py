# test: 新增爬虫文件，生成txt在result/目录下（step 1）ddl
import requests
import re
# 浏览一个网页
url = 'http://www.biquge.info/1_1173/'
# 模拟浏览器发出请求
response = requests.get(url)
# 编码方式
response.encoding = 'UTF-8'
# 目标小说网页源码
html = response.text
# 小说名称
title = re.findall(r'<meta property="og:novel:book_name" content="(.*?)"/>',html)[0]
# 新建文件夹，保存小说内容

# 获取小说每一章信息
dl = re.findall(r'<div id="list">.*?</dl>',html,re.S)[0]
chapter_info_list = re.findall(r'<dd><a href="(.*?)" title="(.*?)">(.*?)</a></dd>',dl)

