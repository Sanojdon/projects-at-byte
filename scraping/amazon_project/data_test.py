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

browser = webdriver.Firefox()
time.sleep(3)
url = "https://www.amazon.in/Fabseasons-Printed-Frills-Automatic-Umbrella/dp/B071VR7RFV/ref=sr_1_1_sspa?s=luggage&ie=UTF8&qid=1510680325&sr=1-1-spons&nodeID=2917474031&psd=1&keywords=umbrella&psc=1"
browser.get(url)

soup = souping()
g = soup.find_all('span', attrs={'id' : "productTitle"})
for span in g.find_all('span'):
	print(span)
