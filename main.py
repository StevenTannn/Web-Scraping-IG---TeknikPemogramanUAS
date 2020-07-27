# -*- coding: utf-8 -*-
import urllib.request
try: #python3
    from urllib.request import urlopen
except: #python2
    from urllib2 import urlopen
from collections import Counter
from scrapeigfunc import last_recent_post,download_ig_photo,post_link_detail,generate_csv

print ("Halo, Welcome To Instagram Web Scraper By 18TI2")
username = input("Please input username that you wanna scrape : ")
count_post = int(input("Please input how many post you wanna scrape (Recommended 3 because its take a long time to scrape) : "))
print ("Loading to get post link one by one")
post_urllink = last_recent_post(username,count_post)
print ("Here are the post link that we aleardy scrape")
print(post_urllink)
filename = username
print ("Please wait for a couple minutes because the photo are being saved in folder images")
post_foto = [download_ig_photo(url,filename, username) for url in post_urllink]
print ("Please wait for a couple minutes because the detail of post are being process")
post_detail = [post_link_detail(url) for url in post_urllink]
print ("Please wait for a couple minutes because we are generating the report for you")
generatecsv = generate_csv(post_detail,username)
print ("The scrape result have been saved in csv folder")
print ("Halo, The Process of scrape" + username + "has been done succesfully")