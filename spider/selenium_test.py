from selenium import webdriver

brower = webdriver.Chrome(executable_path="F:/chromedriver.exe")
brower.get("https://bbs.csdn.net/forums/ios")
print(brower.page_source)