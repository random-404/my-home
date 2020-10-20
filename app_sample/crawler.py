# test: 新增爬虫文件，生成txt在result/目录下（step 1）ddl
import requests
import re
# 浏览一个网页
from bs4 import BeautifulSoup

url = 'https://news.whu.edu.cn/wdyw.htm'
# 模拟浏览器发出http请求
response = requests.get(url)
# 编码方式
response.encoding = 'utf-8'
# 网页源码
html = response.text
soup = BeautifulSoup(html,"html.parser")
list_content = soup.find("div","list")
# print(list_content)
# 提取每一条新闻内容
div = re.findall(r'<div class="list" style="height: 270px">.*?</div>',html,re.S)
list_obj = list_content.find_all("li")
list_obj.remove(list_obj[0])
news_info_list = []
for x in list_obj:
    news_info = re.findall(r'<a class="gray" href="(.*?)" title="(.*?)">', str(x))[0]
    news_info_list.append(news_info)
    s = (news)
    news_info_list.append(s)
print(news_info_list)
print(len(news_info_list))

# news_info_list = []
# pagenum = 1
# error = []
# def getOnePage(url):
#     if url:
#         response = requests.get(url)
#         # 编码方式
#         response.encoding = 'utf-8'
#         # 网页源码
#         html = response.text
#         soup = BeautifulSoup(html, "html.parser")
#         list_content = soup.find("div", "list")
#         # print(list_content)
#         # 提取每一条新闻内容
#         list_obj = list_content.find_all("li")
#         list_obj.remove(list_obj[0])
#         for x in list_obj:
#             try:
#                 news_info = re.findall(r'<a class="gray" href="(.*?)" title="(.*?)">', str(x))[0]
#                 news_info_list.append(news_info)
#             except:
#                 error.append(str(x))
#                 continue
#         print(len(news_info_list))
#         next_page_url = re.findall(r'上页</a><a href="(.*?).htm" class="Next">下页</a>', html)
#         if next_page_url:
#             # <a href="441.htm" class="Next">下页</a>
#             print(next_page_url)
#             print("https://news.whu.edu.cn/wdyw/" + str(next_page_url[0])+".htm")
#             return getOnePage("https://news.whu.edu.cn/wdyw/" + str(next_page_url[0])+".htm")
#
#
#
# getOnePage(url)
#
# print(error)
# print(len(error))
# print("final result:",len(news_info_list))
# print(len(set(news_info_list)))
