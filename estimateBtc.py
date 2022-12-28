import requests
import pandas as pd

# Kripto para birimi simgesi (örneğin: BTC, ETH, LTC)
symbol = "BTC"

# API anahtarını ayarlama
api_key = "YOUR_API_KEY"

# Kripto para birimi değerini çekme
url = f"https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"

querystring = {"symbol":symbol}

headers = {
    "X-CMC_PRO_API_KEY": api_key
}

response = requests.request("GET", url, headers=headers, params=querystring)

data = response.json()["data"][symbol]

# Değerleri veri çerçevesine yükleme
df = pd.DataFrame.from_dict(data, orient="index")

# Değerleri ekrana yazdırma
print(df)
