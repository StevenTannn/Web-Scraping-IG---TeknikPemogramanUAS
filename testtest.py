import pandas as pd
import time
from selenium.webdriver import Chrome

def recent_25_posts(username):
    url = "https://www.tokopedia.com/search?st=product&q=" + username 
    browser = Chrome()
    browser.get(url)
    link_post = []
    while len(link_post) < 10:
        links = browser.find_elements_by_xpath('//*[@id="zeus-root"]/div/div[2]/div/div[2]/div[3]/div[1]/a/div[2]/div[2]/span')[0]
        linktext = links.text
        for link in linktext:
            if link not in link_post:
                link_post.append(link)
        scroll_down = "window.scrollTo(0, document.body.scrollHeight);"
        browser.execute_script(scroll_down)
        time.sleep(10)
    else:
        return link_post[:10]

sneakers_url = recent_25_posts("note10");

print(sneakers_url);


css-1bjwylw

linktext = html.find_all('span', {'class': 'css-1bjwylw'})
for span in spans:
    print(span.text.replace('USD', '').strip())
