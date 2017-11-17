import csv
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from lxml import html

print("Scraping File")
#Assigning the URL to get the content
r = requests.get("https://oyc.yale.edu/political-science/plsc-114")
html = r.content

soup = BeautifulSoup(html, "html.parser")
table = soup.find('table', attrs={'class' : 'views-table'})

lor = []
base_url = "https://oyc.yale.edu"
for row in table.findAll('tr'):
	loc = []
	for cell in row.findAll('td'):
		text = cell.text.replace('\n', '')
		loc.append(cell.text.strip())
	for link in row.findAll('a'):
		loc.append(base_url + link.get('href'))
	lor.append(loc)

# print(lor)
with open('csvs/oyc_lecture.csv', 'w') as csv_file:
	writer = csv.writer(csv_file)
	writer.writerow(["Lecture Number","Topic", "URL"])
	writer.writerows(lor)

# links = []
# for link in table.findAll('a'):
#     links.append(link.get('href'))
#print(links)

# 
# remove_none = [x for x in links if x is not None]
# proper_links = [link for link in remove_none if "lecture" in link]

# full_links = [base_url + link for link in links]

# print(full_links)
