import csv
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from lxml import html

url = "https://www.amazon.in/EPIC-Multicolor-Multi-colour-Colourful-Bumbershoot/dp/B075PJNLCB/ref=pd_sbs_198_4?_encoding=UTF8&psc=1&refRID=YVRB0P77JN4VWXCYSJTW"
r = requests.get(url)
html = r.content
final_list = []

try:
	soup = BeautifulSoup(html, "html.parser")
	title_span = soup.find('span', attrs={'id' : 'productTitle'})
	title = title_span.text.strip()
	print("Product :", title)
	final_list.append(title)
except:
	print("No title")

try:
	price_span = soup.find('span', attrs={'id' : 'priceblock_ourprice'})
	price = price_span.text
	print("Price : ", price)
	final_list.append(price.strip())
except:
	print("No Price")

try:
	table = soup.find('table', attrs={'id' : 'productDetailsTable'})
	content = table.find('div', attrs={'class' : 'content'})
	ul = content.find('ul')
	links = []
	for li in ul.findAll('li'):
		ch = li.text.replace('\n','')
		links.append(ch)
	dime = {}
	for i in range(len(links)-1):
		var = links[i].split(":")
		dime[var[0]] = var[1].strip()
	print(dime)
except:
	print("No details")

for k,v in dime.items():
	if(k == "Product Dimensions"):
		final_list.append(v)
	elif(k == "Item model number"):
		final_list.append(v)
	elif(k=="ASIN"):
		final_list.append(v)
	elif(k=="Average Customer Review"):
		final_list.append(v)
	elif(k=="Date first available at Amazon.in"):
		final_list.append(v)
print("The final list is ")
print(final_list)