from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from scrape import urlmain
from saveimage import filenamelist

html = urlopen(urlmain)
bs = BeautifulSoup(html, 'html.parser')
images = bs.find_all('img', {'src': re.compile('.jpg')})
imagelist = []
for image in images:
    imagelist.append(image['src'])
    print(image['src'] + '\n')
print(filenamelist)
# Test
