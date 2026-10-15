
import requests

res = requests.get('https://nasional.kompas.com/read/2026/10/15/10500031/korupsi-di-tengah-bencana--mana-rasa-kemanusiaan-')

print(res.status_code)
print(res.content)