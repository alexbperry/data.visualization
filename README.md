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



# Homework 2 — Fertility Rate Visualizations

## Q1: Global Fertility Comparisons and Trends

This question explores global fertility patterns using a dataset of total fertility rates from 1800–2020. I reshaped the dataset from wide to long format and produced two visualizations: one showing the top 20 highest fertility rates in the year 2000, and another showing long-term fertility trends for selected countries.

### Tasks Completed
- Converted the dataset from wide to long format using `pandas.melt`.
- Saved the reshaped dataset as `fertility_long.csv`.
- Created a bar chart of the **top 20 fertility rates in 2000**.
- Created a multi-line chart showing **fertility trends over time (1800–2020)** for:
  - Afghanistan  
  - United States  
  - China  
  - India  
  - Nigeria  

### Visualizations
#### 📊 Top 20 Fertility Rates in 2000
![Top 20 Fertility Rates](fertility_snapshot_2000.png)

#### 📉 Fertility Rate Trends Over Time (1800–2020)
![Fertility Trends](fertility_trends.png)

### Code
All data processing and visualization steps were done in Python using Pandas, Matplotlib, and Seaborn.

`reshape_and_plot.py` — full code used for reshaping and plotting.  
<details>
<summary>Click to view code</summary>

```python
:contentReference[oaicite:0]{index=0}


