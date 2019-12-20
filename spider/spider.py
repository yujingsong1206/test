import re
import ast
from urllib import parse

import requests

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

if __name__ == "__main__":
    print(get_last_urls())