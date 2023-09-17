import requests
from bs4 import BeautifulSoup
import sys
import urllib.request
from PIL import Image

name = 'BAY121'
url = 'https://korter.ae/ashjar-at-al-barari-dubai'

r = requests.get(url=url)

r = r.text

a1 = r.find('imageType":"photo","src":"')
a2 = r[a1+19:]
a3 = a2.find('"}}}],')
a4 = a2[:a3+1]

b1 = a4.split(',')
print(b1)
count = 1
img = 1
lst = []
for i in b1:
    q1 = i.find('https://')
    q2 = i.rfind('"')
    q3 = i[q1:q2]
    if '2560x1920' in q3 and q3 not in lst:
        lst.append(q3)

for i in lst:
    urllib.request.urlretrieve(i, f"{name}-{img}.jpg")
    img += 1
    count += 1
