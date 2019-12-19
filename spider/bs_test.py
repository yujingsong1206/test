from bs4 import BeautifulSoup

str = """
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Python基本信息</title>
</head>
<body>
    <div id="info">
        <p>Python信息</p>
        <div id="info-python">
            python牛b（破音）
            <p class="age">年龄: 18</p>
            <p class="name">姓名: tom</p>
            <p class="position">职位: python开发工程师</p>
        </div>
    </div>
</body>
</html>
"""
# bs = BeautifulSoup(str, "html.parser")
# title_tag = bs.title
# print(title_tag.string)
# name_tag = bs.find("p", {"class":"age"})
# print(name_tag.string)
# 学习其实就是对应库的API 接口
# xpatch语法 css选择器
# lxml twists scrapy
# https://www.lfd.uci.edu/~gohlke/pythonlibs/
# pip install lxml-4.4.2-cp37-cp37m-win_amd64.whl
# pip install Twisted-19.10.0-cp37-cp37m-win_amd64.whl
# pip intall Scrapy-1.8.0-py2.py3-none-any.whl

from scrapy import Selector
sel = Selector(text=str)
text_tage = sel.xpath('//div[@id="info-python"]/p[1]/text()|//div[@id="info-python"]/p[2]/text()').extract()
print(text_tage[0],text_tage[1])

# csdn爬取论坛帖子需求
# 抓取策略