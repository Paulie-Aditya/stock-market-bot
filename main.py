import config
import requests

keywords = "tesco"
url = f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={keywords}&apikey={config.api_key}'
r = requests.get(url)
data = r.json()

print(data)