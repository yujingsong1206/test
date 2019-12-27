from datetime import datetime
import re
import ast
from urllib import parse

from selenium import webdriver
from scrapy import Selector
import requests

from spider_text.models import *

def get_html(url):
    brower = webdriver.Chrome(executable_path="F:/chromedriver.exe")
    brower.get(url)
    return brower.page_source

domian = "https://bbs.csdn.net"
def get_nodes_list():
    left_menu_text = requests.get("https://bbs.csdn.net/dynamic_js/left_menu.js?csdn").text
    nodes_str_match = re.search("forumNodes: (.*])", left_menu_text)
    if nodes_str_match:
        nodes_str = nodes_str_match.group(1).replace("null", "None")
        nodes_list = ast.literal_eval(nodes_str)
        return nodes_list
    return []

url_list = []
def process_nodes_list(nodes_list):
    # 将转换的nodes_list提取里面的url
    for item in nodes_list:
        if "url" in item and item["url"]:
            url_list.append(item["url"])
            if "children" in item:
                process_nodes_list(item["children"])

def get_level1_list(nodes_list):
    level1_url = []
    for item in nodes_list:
        if "url" in item and item["url"]:
            level1_url.append(item["url"])
    return level1_url

def get_last_urls():
    nodes_list = get_nodes_list()
    process_nodes_list(nodes_list)
    level1_url = get_level1_list(nodes_list)
    last_urls = []
    for url in url_list:
        if url not in level1_url:
            last_urls.append(parse.urljoin(domian, url))
            last_urls.append(parse.urljoin(domian, url + "/recommend"))
            last_urls.append(parse.urljoin(domian, url + "/closed"))
    return last_urls


def parse_topic(url):
    # 获取帖子的详情和回复
    topic_id = url.split("/")[-1]
    rest_text = get_html(url)
    sel = Selector(text=rest_text)
    all_divs = sel.xpath('//div[starts-with(@id, "post-")]')
    topic_item = all_divs[0]
    content = topic_item.xpath('.//div[@class="post_body post_body_min_h"]').extract()[0]
    praised_nums = int(topic_item.xpath('.//label[@class="red_praise digg"]//em/text()').extract()[0])
    jtl_str = topic_item.xpath('.//div[@class="close_topic"]/text()').extract()[0]
    jtl_match = re.search("(\d+)", jtl_str)
    jtl = 0
    if jtl_match:
        jtl = jtl_match.group(1)
    existed_topics = Topic.select().where(Topic.id == topic_id)
    if existed_topics:
        topic = existed_topics[0]
        topic.content = content
        topic.parised_nums = praised_nums
        topic.jtl = float(jtl)
        topic.save()

def parse_list(url):
    rest_text = get_html(url)
    sel = Selector(text=rest_text)
    all_trs = sel.xpath('//table[@class="forums_tab_table"]//tbody//tr')
    for tr in all_trs:
        status = tr.xpath('.//td[1]/span/text()').extract()[0]
        score = int(tr.xpath('.//td[2]/em/text()').extract()[0])
        topic_url = parse.urljoin(domian, tr.xpath('.//td[3]/a[last()]/@href').extract()[0])
        topic_title = tr.xpath('.//td[3]/a[last()]/text()').extract()[0]
        author_url = tr.xpath('.//td[4]/a/@href').extract()[0]
        author_id = author_url.split("/")[-1]
        create_time_str = tr.xpath('.//td[4]/em/text()').extract()[0]
        create_time = datetime.strptime(create_time_str, "%Y-%m-%d %H:%M")
        answer_info = tr.xpath('.//td[5]/span/text()').extract()[0]
        answer_nums = int(answer_info.split("/")[0])
        click_nums = int(answer_info.split("/")[1])
        last_time_str = tr.xpath('.//td[6]/em/text()').extract()[0]
        last_time = datetime.strptime(last_time_str, "%Y-%m-%d %H:%M")

        topic = Topic()
        topic.status = status
        topic.score = score
        topic.title = topic_title
        topic.author = author_id
        topic.create_time = create_time
        topic.last_time = last_time
        topic.answer_nums = answer_nums
        topic.click_nums = click_nums
        topic.id = int(topic_url.split("/")[-1])

        existed_topic = Topic.select().where(Topic.id == topic.id)
        if existed_topic:
            topic.save()
        else:
            topic.save(force_insert=True)

        parse_topic(topic_url)

if __name__ == "__main__":
    last_urls = get_last_urls()
    parse_list(last_urls[0])