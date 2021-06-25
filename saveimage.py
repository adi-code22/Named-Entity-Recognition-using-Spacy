import urllib.request
from image import imagelist
# imgURL = "http://site.meishij.net/r/58/25/3568808/a3568808_142682562777944.jpg"
filenamelist = []
for imgURL, index in imagelist:
    urllib.request.urlretrieve(("https:" + imgURL), ("D:/filename" + index + ".jpg"))
    print("D:/filename" + index + ".jpg")
    filenamelist.append("D:/filename" + index + ".jpg")

