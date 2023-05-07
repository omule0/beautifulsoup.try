import sys
import requests
import time
import os
from bs4 import BeautifulSoup
from selenium import webdriver
import csv

url = 'https://techcabal.com/2023/04/18/autochek-acquires-majority-stake-in-egypts-autotager/?mc_cid=d70902c579&mc_eid=3e21a91cc9'

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get(url)

html_text = driver.page_source

soup = BeautifulSoup(html_text,'lxml') 

articles = soup.find_all('div', class_ = "single-article-main")



with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)

    # loop through each article element and extract the title and text
    for article in articles:
        title = article.find('h2').text
        paragraphs = article.find_all('p')
        text = '\n'.join([p.text for p in paragraphs])
        writer.writerow([title, text])

# close the webdriver
driver.quit()




