
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://data.go.id/dataset/dataset/jumlah-anak-terlantar-tahun-2023"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

titles = soup.find_all("li")

data = []

for item in titles:
    data.append(item.get_text(strip=True))

print(data)

df = pd.DataFrame(data, columns=["title"])
df.to_csv("data_anak_terlantar.csv", index=False)
