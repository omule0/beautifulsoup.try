import sys
import requests 
import time
import os
from bs4 import BeautifulSoup
from selenium import webdriver
import csv
import datetime

url = input('Please enter the website URL you want to scrap: ')
print(f'The URL {url} has been received')

tag = input('Please enter the html tag used for the article: ')
print(f'The selector {class_} has been received')

class_ = input('Please enter the CSS selector/class for the article: ')
print(f'The selector {class_} has been received')



driver = webdriver.Chrome()
driver.implicitly_wait(30) 
driver.get(url)

html_text = driver.page_source   

soup = BeautifulSoup(html_text,'lxml')   

articles = soup.find_all(tag, class_) 

now = datetime.datetime.now()
filename = now.strftime("%Y-%m-%d-%H-%M-%S") + '.csv'

with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)

    # loop through each article element and extract the title and text
    for article in articles:
        title = article.find('h2').text
        paragraphs = article.find_all('p')
        text = '\n'.join([p.text for p in paragraphs])
        writer.writerow([title, text])

# close the webdriver
driver.quit()