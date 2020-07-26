import pandas as pd
import time
from selenium.webdriver import Chrome

def recent_25_posts(username):
    url = "https://www.instagram.com/" + username 
    browser = Chrome()
    browser.get(url)
    post = 'https://www.instagram.com/p/'
    link_post_temp=[]
    link_post = []
    while len(link_post) < 10:
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
        return link_post[:10]

sneakers_url = recent_25_posts("sistech.uphmedan");

print(sneakers_url);

