
import requests
import pandas as pd
from bs4 import BeautifulSoup
import re

print("getting urls")

url = 'https://semi-rad.com/category/friday-inspiration/'

st = ""
req = requests.get(url, verify=False).text
soup = BeautifulSoup(req, 'lxml')
snip = soup.findAll('div', 'social-sharing')
for i in range(len(snip)):
    st += snip[i]['data-permalink'] + '\n'


for page in [2, 3, 4, 5, 6, 7, 8]:

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
