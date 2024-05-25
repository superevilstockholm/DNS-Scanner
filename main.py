import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import time
import pandas as pd

session = requests.Session()

ua = UserAgent()
session.headers.update({'User-Agent': ua.random})

url = "https://dnsdumpster.com/"

get_response = session.get(url)
soup = BeautifulSoup(get_response.content, 'html.parser')
csrf_token = soup.find('input', {'name': 'csrfmiddlewaretoken'}).get('value')

url_target = input("Masukkan url website yang ingin di scan: ")

headers = {
    'Referer': 'https://dnsdumpster.com/'
}

data = {
    'targetip': str(url_target),
    'user': 'free'
}

session.headers.update({'X-CSRFToken': csrf_token})

post_response = session.post(url, data=data, headers=headers)

out_soup = BeautifulSoup(post_response.content, 'html.parser')

time.sleep(7)

tables = out_soup.find_all('table')

dfs = []

pd.set_option('display.max_colwidth', None)

for table in tables:
    for tag in table.find_all(['a', 'form']):
        tag.decompose()
    table_data = []
    for row in table.find_all('tr'):
        row_data = [cell.get_text(strip=False).replace("\n\n\n\n\n\n\n", " - ").replace("\n\n\n \n\n\n", "").replace("\n\n\n\n\n", "").replace("\n", " ") for cell in row.find_all(['th', 'td'])]
        table_data.append(row_data)
    if table_data:
        df = pd.DataFrame(table_data, columns=None)
        dfs.append(df)

for i, df in enumerate(dfs, 1):
    if i == 1:
        print(f"DataFrame (DNS servers):")
    elif i == 2:
        print(f"DataFrame (MX records):")
    elif i == 3:
        print(f"DataFrame (TXT records):")
    elif i == 4:
        print(f"DataFrame (HOST records (A) ):")
    else:
        print('Untitled DataFrame')
    print(df)
    print()