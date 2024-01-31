import requests
from bs4 import BeautifulSoup as BS
import pandas as pd

URL = 'https://www.footballdb.com/fantasy-football/index.html?pos=OFF&yr=2023&wk=1&key=b6406b7aea3872d5bb677f064673c57f'

res = requests.get(URL)
soup = BS(res.content, 'html.parser')

print('Soup', soup)
# table = soup.find('table', {'id': 'fantasy'})
# df = pd.read_html(str(table))[0]
# df.columns = df.columns.droplevel(level=0)

# df.head()