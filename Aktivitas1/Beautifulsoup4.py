import requests
from bs4 import BeautifulSoup

url = "https://nasional.kompas.com/read/2026/10/15/10500031/korupsi-di-tengah-bencana--mana-rasa-kemanusiaan-"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

title = soup.find_all('div', class_='wrap')
for item in title:
    print(item.get_text(strip=True))
