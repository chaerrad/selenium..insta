
from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import shutil
import time



#opener = urllib.request.build_opener()
#opener.addheaders = [
#    ('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
#urllib.request.install_opener(opener)

search_name = input("검색어를 입력하세요: ")



baseurl = "https://www.instagram.com/explore/tags/"
plusurl = search_name
url = baseurl + quote_plus(plusurl)

driver = webdriver.Chrome()
driver.get(url)

# 로그인시간
time.sleep(30)

html = driver.page_source
soup = BeautifulSoup(html)

imgList = []

insta = soup.select('.v1Nh3.kIKUG._bz0w')

SCROLL_PAUASE_TIME = 1.5

while True:
    time.sleep(SCROLL_PAUASE_TIME)
    last_height = driver.execute_script("return document.body.scrollHeight")
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(SCROLL_PAUASE_TIME)
    new_height = driver.execute_script("return document.body.scrollHeight")   
    for i in insta:
        print('https://www.instagram.com' + i.a['href'])
        imgUrl = i.select_one('.KL4Bh').img['src']
        imgList.append(imgUrl)
        imgList = list(set(imgList))
        html = driver.page_source
        soup = BeautifulSoup(html)
        insta = soup.select('.v1Nh3.kIKUG._bz0w')
    if new_height == last_height: 
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") 
        time.sleep(SCROLL_PAUASE_TIME) 
        new_height = driver.execute_script("return document.body.scrollHeight") 
        if new_height == last_height: 
            break 
        else: 
            last_height = new_height 
            continue

    
    time.sleep(2)


n=0

for i in range(0,100000000000000000000):
    imageurl = imgList[n]
    with urlopen(imageurl) as f:
        with open('./img/' + 'insta' + str(n)+ '.jpg', 'wb')as h:
            img = f.read()
            h.write(img)
    n+=1
    

driver.close()