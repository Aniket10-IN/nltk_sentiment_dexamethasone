from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

import pandas as pd
from bs4 import BeautifulSoup
import requests

s = Service('/home/aniket/Documents/chromedriver_linux64/chromedriver')
driver = webdriver.Chrome(service= s)
driver.get('https://www.reddit.com/search/?q=dexamethasone%20covid')
time.sleep(3)

def scroll(driver, wait_time):
    time.sleep(wait_time)
    
    height = driver.execute_script('return document.body.scrollHeight')
    while True:
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(5)
        new_height = driver.execute_script('return document.body.scrollHeight')
        if height == new_height:
            break

        height = new_height

def all_posts(url):
    driver = webdriver.Chrome(service= s)
    driver.implicitly_wait(20)
    driver.get(url)
    scroll(driver, 5)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    driver.close()
    
    posts = []
    
    for data in soup.find_all("h3", class_="_eYtD2XCVieq6emjKBH3m"):
        posts.append(data.text)
        
    return posts