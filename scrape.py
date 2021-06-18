# Import packages
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# Specify url of the web page
# topic = []
topic = input("Enter the topic to be searched in Wikipedia: ")
# topic.append(name)
# Configuring the word for wikipedia url
# for ele in topic:
#     # adding each string after replacement using replace()
#     topic.append(ele.replace(" ", "_"))
source = urlopen("https://en.wikipedia.org/wiki/" + topic).read()

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


