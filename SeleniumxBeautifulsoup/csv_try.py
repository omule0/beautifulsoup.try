import sys
import requests
import time
import os
from bs4 import BeautifulSoup
from selenium import webdriver
import csv


print('Please enter the website you want to scrap')
website = input('>')
print(f'website has been sent')

url = website

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get(url)

html_text = driver.page_source

soup = BeautifulSoup(html_text,'lxml') 

# make some inputs automatic

articles = soup.find_all('article', class_ = "post-31949 post type-post status-publish format-standard has-post-thumbnail category-news category-west-africa tag-featured tag-storspay tag-techstars")

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

