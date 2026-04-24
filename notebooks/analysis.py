#market density by state 
state_counts = df["phy_state"].value_counts().reset_index()
state_counts.columns = ["state", "companies"]

state_counts.head(10)

#find the dominating market 
total_companies = state_counts["companies"].sum()

state_counts["market_share_%"] = (
    state_counts["companies"] / total_companies * 100
)

#Small vs Large Carrier Segmentation
df["fleet_group"] = df["fleetsize"].map({
    "A": "1 truck",
    "B": "2-3",
    "C": "4-6",
    "D": "7-8",
    "E": "9-11"
})

df["fleet_group"].value_counts()

#High-Value Segments
hazmat = df["hm_ind"].value_counts(normalize=True) * 100
hazmat

#visual of companies per state for better understanding 
import matplotlib.pyplot as plt

state_counts.head(10).plot(
    kind="bar",
    x="state",
    y="companies",
    title="Top States by Carrier Density"
)

plt.show()

