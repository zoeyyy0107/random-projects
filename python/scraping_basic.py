import requests
from bs4 import BeautifulSoup
from lxml import etree
import pandas as pd
from concurrent.futures import ThreadPoolExecutor

finalData = []
url = ''
response = requests.get(url)

# BeautifulSoup
soup = BeautifulSoup(response.content, 'lxml')
dom = etree.HTML(str(soup))

# multiprocessing
def Scrape(url):
    print(f'Scraping {url}...')
    response = requests.get(url)
    return response.json()

iterableList = []
results = []
pool = ThreadPoolExecutor(max_workers=10)
for page in pool.map(Scrape, iterableList):
    results.append(page)

# Output
df = pd.DataFrame(finalData)
df.to_csv('output\Best Friends Network Partner.csv', index=False)