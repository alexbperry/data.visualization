import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

INPUT = Path("children_per_woman_total_fertility (2).csv")  
df = pd.read_csv(INPUT)

print("Preview of data:")
print(df.head())

long_df = df.melt(id_vars=["country"], var_name="year", value_name="fertility_rate")

long_df["year"] = pd.to_numeric(long_df["year"], errors="coerce")

long_df.to_csv("fertility_long.csv", index=False)


plt.figure(figsize=(12,6))
snapshot_2000 = long_df[long_df["year"] == 2000]

sns.barplot(data=snapshot_2000.sort_values("fertility_rate", ascending=False).head(20),
            x="country", y="fertility_rate", palette="viridis")

plt.xticks(rotation=75)
plt.title("Top 20 Fertility Rates in 2000 (Children per Woman)", fontsize=14)
plt.xlabel("Country")
plt.ylabel("Children per Woman")
plt.tight_layout()
plt.savefig("fertility_snapshot_2000.png")
plt.close()

plt.figure(figsize=(12,6))
countries = ["Afghanistan", "United States", "China", "India", "Nigeria"]  

for c in countries:
    subset = long_df[long_df["country"] == c]
    plt.plot(subset["year"], subset["fertility_rate"], label=c)

plt.title("Fertility Rate Trends Over Time (1800–2020)", fontsize=14)
plt.xlabel("Year")
plt.ylabel("Children per Woman")
plt.legend()
plt.tight_layout()
plt.savefig("fertility_trends.png")
plt.close()

print("Charts saved: fertility_snapshot_2000.png and fertility_trends.png")
print("Reshaped data saved as fertility_long.csv")
