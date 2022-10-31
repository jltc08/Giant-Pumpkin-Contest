#https://pythonbasics.org/pandas-web-scraping/
 
#Install Modules

from multiprocessing.managers import BaseManager
import lxml 
import html5lib 
import bs4
import pandas as pd
import openpyxl

#Pandas Web Scraping
# Webpage url                                                                                                               
url = 'http://www.bigpumpkins.com/WeighoffResultsGPC.aspx?c=P&y=2022'

# Extract tables
dfs = pd.read_html(url)

# Get first table                                                                                                           
df = dfs[0]

# Extract columns                                                                                                           
df2 = df[['Place','Weight (lbs)', 'Grower Name', 'City', 'State/Prov',	'Country', 'GPC Site',	'Seed (Mother)',	'Pollinator (Father)',	'OTT',	'Est. Weight',	'Pct. Chart']]
print(df2)

# Write to excel
df2.to_excel(r'/Users/tbrown/Documents/pumpkin_python.xlsx')

#Success!
