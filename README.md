# data.visualization
A set of data visualization projects where I explore datasets and improve my skills in analysis and visual storytelling.

# Homework 1 – Story Structure

This project analyzes the storytelling approach used in *Storytelling With You* by Cole Nussbaumer Knaflic. I identified the structure she used, broke down the key elements of her narrative, and then re-created the same story using an alternate structure.

## Key Work
- Identified that Cole used the **OCAR** story structure.
- Outlined the **O**, **C**, **A**, and **R** elements from her presentation.
- Re-told the same story in a different structure (**ABDCE**) to compare how narrative framing influences the story.

## Files
- `Homework1_StoryStructure.docx` — full written responses.



# Homework 2 – Q1: Fertility Rate Visualizations

This question explores global fertility patterns using a dataset of total fertility rates from 1800–2020. I reshaped the dataset from wide to long format and created two visualizations: one showing the countries with the highest fertility rates in the year 2000, and another showing long-term fertility trends for selected countries.

## Tasks Completed

- Loaded the fertility dataset from CSV.
- Reshaped the data from wide to long format using `pandas.melt`.
- Converted the `year` column to numeric and saved the long-format data as `fertility_long.csv`.
- Created:
  - A bar chart of the **top 20 fertility rates in 2000**.
  - A line chart of **fertility trends (1800–2020)** for:
    - Afghanistan  
    - United States  
    - China  
    - India  
    - Nigeria  

## Visualizations

> Make sure this README is in the same folder as the images (or update the paths if not).

### 📊 Top 20 Fertility Rates in 2000
![Top 20 Fertility Rates in 2000](Homework 2\Story_Structure\q1\fertility_snapshot_2000.png)

### 📉 Fertility Rate Trends Over Time (1800–2020)
![Fertility Rate Trends Over Time](Homework 2\Story_Structure\q1\fertility_trends.png)

## Code

```python
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
