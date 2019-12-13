from bs4 import BeautifulSoup

html = """
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
bs = BeautifulSoup(html, "html.parser")
title_tag = bs.title
print(title_tag.string)
name_tag = bs.find("p", {"class":"age"})
print(name_tag.string)