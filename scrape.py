# Import packages
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

topic = input("Enter the topic to be searched in Wikipedia: ")
topic = topic.replace(" ", "_")
print(topic)
urlmain = "https://en.wikipedia.org/wiki/" + topic
source = urlopen(urlmain).read()

# Make a soup
soup = BeautifulSoup(source, 'lxml')

# Extract the plain text content from paragraphs
paras = []
for paragraph in soup.find_all('p'):
    paras.append(str(paragraph.text))

# Extract text from paragraph headers
heads = []
for head in soup.find_all('span', attrs={'mw-headline'}):
    heads.append(str(head.text))

# Interleave paragraphs & headers
text = [val for pair in zip(paras, heads) for val in pair]
text = ' '.join(text)

# Drop footnote superscripts in brackets
text = re.sub(r"\[.*?\]+", '', text)

# Replace '\n' (a new line) with '' and end the string at $1000.
text = text.replace('\n', '')[:-11]
print(text)


