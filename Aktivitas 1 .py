import requests
from bs4 import BeautifulSoup

#Request Module
import requests
res = requests.get("https://data.go.id/dataset/dataset/jumlah-anak-terlantar-tahun-2023")
print(res.status_code)
print(res.content)

#BeautifulSoup1
url = "https://data.go.id/dataset/dataset/jumlah-anak-terlantar-tahun-2023"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

title = soup.title

print(title)

#BeautifulSoup2

url = "https://data.go.id/dataset/dataset/jumlah-anak-terlantar-tahun-2023"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

title = soup.find("h1")
print(title)

#BeautifulSoup3

import requests
from bs4 import BeautifulSoup

url = "https://data.go.id/dataset/dataset/jumlah-anak-terlantar-tahun-2023"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

title = soup.find_all("div", class_="header_nav_el_mobile")

for item in title:
    print(item.get_text(strip=True))
