***pull data***

import pandas as pd
import requests

url = "https://data.transportation.gov/resource/az4n-8mr2.json"

params = {
    "$limit": 100000  # start manageable
}

response = requests.get(url, params=params)
data = response.json()

df = pd.DataFrame(data)

df.head()
