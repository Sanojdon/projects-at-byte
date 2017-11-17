#For Datascraping from the webpage
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

#For csv data binding
import csv
import requests
from bs4 import BeautifulSoup
from lxml import html

#For database operations
import sqlite3
import sys

def souping():
	new_url = browser.current_url
	req = requests.get(new_url)
	html = req.content
	soup = BeautifulSoup(html, "html.parser")
	return soup


search_items = ['umbrella', 'fidget spinner']
browser = webdriver.Firefox()
time.sleep(3)
url = "https://www.amazon.in"
browser.get(url)
print("Connected to amazon.in..")

for i in range(0,1):
	inp = browser.find_element_by_id("twotabsearchtextbox")
	inp.send_keys(search_items[i])
	inp.send_keys(Keys.ENTER)
	time.sleep(10)
    
    
	soup = souping()
	print("Entered the search box..")

	time.sleep(10)
	ul = soup.find('ul', attrs={'id' : 's-results-list-atf'})
	result = []
	print("Getting Results..")
	#Getting the results
	for li in ul.findAll('li'):
		li = (li.get('id'))
		result.append(li)
	print(result)
	for i in range(len(result)):
		try:
			fr = browser.find_element_by_id(result[i])
			fr.click()
			print("Clicked the element..")
			url = browser.current_url
			r = requests.get(url)
			html = r.content
			try:
				soup = BeautifulSoup(html, "html.parser")
				title_span = soup.find('span', attrs={'id' : 'productTitle'})
				title = title_span.text.strip()
				print("Product :", title)
			except:
				print("No title", sys.exc_info()[0])
			try:
				price_span = soup.find('span', attrs={'id' : 'priceblock_ourprice'})
				price = price_span.text.strip()
				print("Price : ", price)
			except:
				print("No Price", sys.exc_info())
			try:
				table = soup.find('table', attrs={'id' : 'productDetailsTable'})
				content = table.find('div', attrs={'class' : 'content'})
				ul = content.find('ul')
				links = []
				for li in ul.findAll('li'):
					ch = li.text.replace('\n','')
					links.append(ch.strip())
				dime = {}
				for i in range(len(links)-1):
					var = links[i].split(":")
					dime[var[0]] = var[1]
					print(dime)
			except:
				print("No details")
			print("Connected Successfully!!!")
			browser.back()
		except:
			print("Bad Network")










	# for i in range(len(result)):
	# 	try:
	# 		fr = browser.find_element_by_id(result[i])
	# 		fr.click()
	# 		soup = souping()
	# 		print(soup.find('h1', attrs={'id' : 'title'}))
	# 		print("Good Job!!")
	# 		browser.back()
	# 	except:
	# 		print("Bad Network")


	



# browser.execute_script('''window.open("http://stackoverflow.com/","_blank");''')
