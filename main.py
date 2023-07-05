import config
import requests

url = f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=tesco&apikey={config.api_key}'
r = requests.get(url)
data = r.json()

print(data)