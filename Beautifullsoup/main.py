from bs4 import BeautifulSoup
'''with open('bspy.html','r') as html_file:
    content = html_file.read()
    
    soup = BeautifulSoup(content,'lxml') 
    #print(soup.prettify())
    tags = soup.find_all('p')
    for tag in tags:
        words = tag.get_text().split()[1]
        for word in words:
            print(word)
        #print(tag.text)
    #print(tags)'''
import requests
