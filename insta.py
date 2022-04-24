import os
import urllib.request
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

opener = urllib.request.build_opener()
opener.addheaders = [
    ('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)

search_name = input("검색어를 입력하세요: ")
folder_name = input("넣을  폴더 이름을 입력하세요: ")
try:
    os.mkdir(folder_name)
except:
    print("이미 존재하는 폴더입니다")

baseurl = "https://www.instagram.com/explore/tags/"
plusurl = search_name
url = baseurl + plusurl

driver = webdriver.Chrome()
driver.get(url)

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")


while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(3)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height


images = driver.find_elements_by_css_selector(".KL4Bh")
count = 1
for image in images:
    imgUrl = driver.find_elements_by_css_selector(
        ".KL4Bh").get_attribute("src")
    opener = urllib.request.build_opener()
    opener.addheaders = [
        ('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
    urllib.request.install_opener(opener)
    urllib.request.urlretrieve(
        imgUrl, folder_name + "/test" + str(count) + ".jpg")
    count = count+1


driver.close()
