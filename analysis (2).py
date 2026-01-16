import pandas as pd
import requests

url = "https://data.transportation.gov/resource/az4n-8mr2.json"
params = {"$limit": 500000}  # or more
response = requests.get(url, params=params)
df = pd.DataFrame(response.json())

df.head()

df.shape

df.columns

# Standardize column names
df.columns = df.columns.str.lower()

# Replace blanks with NaN
df.replace("", pd.NA, inplace=True)

# Hazmat vs Non-Hazmat
df["hm_ind"].value_counts(dropna=False)

#Carrier Operation
df["carrier_operation"].value_counts(dropna=False)

#Top 10 States
df["phy_state"].value_counts().head(10)

#Produce Hauling
df["crgo_produce"].value_counts(dropna=False)

#Liquid Gas Hauling
df["crgo_liqgas"].value_counts(dropna=False)

#Fleet Size
df["fleetsize"].value_counts().sort_index()

#Total Drivers
df["total_drivers"].value_counts().sort_index()
