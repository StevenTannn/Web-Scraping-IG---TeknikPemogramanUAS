# -*- coding: utf-8 -*-
import pandas as pd
import time
import datetime
import urllib.request
try: #python3
    from urllib.request import urlopen
except: #python2
    from urllib2 import urlopen
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import Firefox
from collections import Counter

def last_5_post(username):
    url = "https://www.instagram.com/" + username 
    options = Options()
    options.add_argument('-headless')
    browser = Firefox(executable_path='geckodriver', options=options)
    browser.get(url)
    post = 'https://www.instagram.com/p/'
    link_post_temp = []
    link_post = []
    while len(link_post) < 2:
        links = browser.find_elements_by_xpath("//a[@href]")
        for a in links:
            link_post_temp.append(a.get_attribute("href"))
        for link in link_post_temp:
            if post in link and link not in link_post:
                link_post.append(link)
        scroll_down = "window.scrollTo(0, document.body.scrollHeight);"
        browser.execute_script(scroll_down)
        time.sleep(10)
    else:
        browser.stop_client()
        return link_post[:2]

def find_hashtags(comment):
    hashtags = re.findall('#[A-Za-z]+', comment)
    if (len(hashtags) > 1) & (len(hashtags) != 1):
        return hashtags
    elif len(hashtags) == 1:
        return hashtags[0]
    else:
        return ""


def find_mentions(comment):
    mentions = re.findall('@[A-Za-z]+', comment)
    if (len(mentions) > 1) & (len(mentions) != 1):
        return mentions
    elif len(mentions) == 1:
        return mentions[0]
    else:
        return ""


def post_link_detail(url):
    options = Options()
    options.add_argument('-headless')
    time.sleep(10)
    browser = Firefox(executable_path='geckodriver', options=options)
    browser.get(url)
    try:
        likes = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[3]/section[2]/div/div/button/span').text.split()[0]
        post_type = 'photo'
    except:
        likes = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[3]/section[2]/div/span/span').text.split()[0]
        post_type = 'video'
    age = browser.find_element_by_css_selector('a time').text
    try:
        comment = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[3]/div[1]/ul/ul[2]/div/li/div/div/div[2]/span').text
        hashtags = find_hashtags(comment)
        mentions = find_mentions(comment)
    except:
        comment = "none"
        hashtags = "none"
        mentions = "none"
    post_details = {'link': url, 'type': post_type, 'likes/views': likes,
                    'age': age, 'comment': comment, 'hashtags': hashtags,
                    'mentions': mentions}
    time.sleep(10)
    return post_details

def download_ig_photo(url,filename):
    options = Options()
    options.add_argument('-headless')
    time.sleep(10)
    browser = Firefox(executable_path='geckodriver', options=options)
    browser.get(url)
    try: 
        image = browser.find_element_by_xpath('/html/body/div[1]/section/main/div/div/article/div[2]/div/div/div[1]/img').get_attribute('src').split(' ')[0]
        y = datetime.datetime.now()
        datetimefile = y.strftime("%d-%b-%Y (%H:%M:%S)")
        filename = username+datetimefile+'.jpg'
        urllib.request.urlretrieve(image, filename)
        print("Gambar telah disimpan")
    except:
        print("Tidak ada gambar,error")

username = 'uphimpactslives'
post_urllink = last_5_post(username)
print(post_urllink)
filename = username
post_foto = [download_ig_photo(url,filename) for url in post_urllink]
post_detail = [post_link_detail(url) for url in post_urllink]
result = pd.DataFrame(post_detail,)
result.head()
x = datetime.datetime.now()
datetime = x.strftime("%d-%b-%Y (%H:%M:%S)")
result.to_csv("csv/"+username+datetime+".csv")