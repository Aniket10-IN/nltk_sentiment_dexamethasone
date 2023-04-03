import pandas as pd
from bs4 import BeautifulSoup
import requests

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

from drugs_webpage_bs4 import webpage
from youtube_comments_api import video_comments
from reddit_reviews_selenium import all_posts

all_comments = []
result = webpage('https://reviews.webmd.com/drugs/drugreview-1027-dexamethasone-oral') #drug page  reviews
for i in result:
    all_comments.append(i)

result = video_comments('jrwSo9ZDZEg') # comments from youtube posts
for i in result:
    all_comments.append(i)

result = video_comments('DSvEjo7feyc') # youtube comments 
for i in result:
    all_comments.append(i)

result = all_posts('https://www.reddit.com/search/?q=dexamethasone%20covid') # reddit comments
for i in result:
    all_comments.append(i)

time.sleep(10)
print(len(all_comments))

df = pd.DataFrame(all_comments, columns = ['comments'])

df.to_csv('comments.csv', index = False)

