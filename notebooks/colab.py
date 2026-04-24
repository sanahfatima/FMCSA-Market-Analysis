#pull data from the fmcsa dataset

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

#clean 

df.columns = df.columns.str.lower().str.strip()

df.replace("", pd.NA, inplace=True)

# Important columns
cols = [
    "phy_state",
    "carrier_operation",
    "hm_ind",
    "fleetsize",
    "total_drivers",
    "crgo_produce",
    "crgo_liqgas"
]

df = df[cols]
