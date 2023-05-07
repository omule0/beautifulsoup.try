import sys
import requests
import time
import os
from bs4 import BeautifulSoup
from selenium import webdriver
import csv


url2 = 'https://disrupt-africa.com/2023/04/28/nigerian-fintech-startup-storspay-raises-320k-selected-for-techstars-nyc/?mc_cid=d70902c579&mc_eid=3e21a91cc9'

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get(url2)

html_text = driver.page_source

soup = BeautifulSoup(html_text,'lxml') 

articles = soup.find_all('article', class_ = "post-31949 post type-post status-publish format-standard has-post-thumbnail category-news category-west-africa tag-featured tag-storspay tag-techstars")


# Check if the file already exists
with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    for article in articles:
        header = article.find('h1', class_ = "post-title item fn").text
        author =article.find('span', class_ = "posted-by").text
        date = article.find('span', class_ = "posted-on").text
        paragraphs = article.find('div', class_ = "post-container cf")
        for paragraph in paragraphs:
            statement = article.find_all('p')
            selected_statements = [p.text for p in statement]
            text = '\n'.join(selected_statements)
    writer.writerow([date, author, header, text])       

