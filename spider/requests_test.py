# 数据采集：1.全网采集 2.全站采集 3.特定网站的特定数据的采集
# 数据获取：1.url获取HTML数据 2.api数据 3.通过开发接口来获取数据
import requests

res = requests.get("http://www.taobao.com")
print(res.text)
