import sys
import requests 
import time
import os
from bs4 import BeautifulSoup
from selenium import webdriver
import csv
import datetime

#automate inputs
url = input('Please enter the website URL you want to scrap: ')
print(f'The URL {url} has been received')

url = input('Please enter the website URL you want to scrap: ')
print(f'The URL {url} has been received')

tag = input('Please enter the html tag used for the article: ')
print(f'The selector {class_} has been received')

class_ = input('Please enter the CSS selector/class for the article: ')
print(f'The selector {class_} has been received')

#initiate selenium driver-chrome driver
driver = webdriver.Chrome()
driver.implicitly_wait(30) 
driver.get(url)

#extract html text
html_text = driver.page_source   

#initiate beautiful soup
soup = BeautifulSoup(html_text,'lxml')    

#find all articles
articles = soup.find_all(tag, class_) 

#uniquely name output files 
now = datetime.datetime.now()
filename = now.strftime("%Y-%m-%d-%H-%M-%S") + '.csv'

#write to csv
with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    #loop

# close the webdriver
driver.quit()
