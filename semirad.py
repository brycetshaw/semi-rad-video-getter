
import requests
import pandas as pd
from bs4 import BeautifulSoup
import re

print("getting urls")


st = ""

url = 'https://semi-rad.com/category/friday-inspiration/'
req = requests.get(url, verify=False).text
soup = BeautifulSoup(req, 'lxml')
snip = soup.findAll('div', 'social-sharing')
for i in range(len(snip)):
    st += snip[i]['data-permalink'] + '\n'


for page in range(1,9):
    url = f"https://semi-rad.com/category/friday-inspiration/page/{page}/"
    req = requests.get(url, verify=False).text
    soup = BeautifulSoup(req, 'lxml')
    snip = soup.findAll('div', 'social-sharing')
    for i in range(len(snip)):
        st += snip[i]['data-permalink'] + '\n'

text_file = open("Friday-inspiration-urls.txt", "w")
text_file.write(st)
text_file.close()

print('File write success. Wrote to \'Friday-inspiration-urls.txt\'')
