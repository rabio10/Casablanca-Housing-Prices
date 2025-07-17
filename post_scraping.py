from bs4 import BeautifulSoup
# prompt: get the necessary lib for making http request to get html document

import requests
import re

file = open('links.txt','r')
links = file.readlines()

# go inside each link
len = links.__len__()
for i in range(len):
  avito_post_link = links[i]
  headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
  markup = requests.get(avito_post_link, headers=headers)
  soup = BeautifulSoup(markup.content, 'html.parser')
  # now we have the soup, lets extract what we want
  
file.close()