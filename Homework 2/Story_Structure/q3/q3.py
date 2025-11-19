import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize, TwoSlopeNorm

def plot_bar(df, fertility, colors, title, colorbar_label=None, norm=None, cmap=None, filename="plot.png"):
    fig, ax = plt.subplots(figsize=(12,6))
    bars = ax.bar(df["country"], fertility, color=colors)
    ax.set_title(title)
    ax.set_ylabel("Children per Woman")
    ax.set_xlabel("Country")
    ax.set_xticklabels(df["country"], rotation=45, ha="right")
    if colorbar_label and norm and cmap:
        sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
        sm.set_array([])
        fig.colorbar(sm, ax=ax, label=colorbar_label)
    plt.tight_layout()
    plt.savefig(filename)
    plt.show()

df = pd.read_csv("fertility_long.csv")
df_2000 = df[df["year"] == 2000].sort_values(by="fertility_rate", ascending=False).head(20)
fertility = df_2000["fertility_rate"].to_numpy()

# Qualitative
plot_bar(
    df_2000, fertility,
    colors=plt.cm.tab20.colors[:len(df_2000)],
    title="Qualitative Color Scale",
    filename="qualitative.png"
)

# Sequential
norm_seq = Normalize(vmin=fertility.min(), vmax=fertility.max())
colors_seq = plt.cm.viridis(norm_seq(fertility))
plot_bar(
    df_2000, fertility,
    colors=colors_seq,
    title="Sequential Color Scale",
    colorbar_label="Fertility Rate",
    norm=norm_seq,
    cmap="viridis",
    filename="sequential.png"
)

# Diverging
mean_val = fertility.mean()
norm_div = TwoSlopeNorm(vmin=fertility.min(), vcenter=mean_val, vmax=fertility.max())
colors_div = plt.cm.RdBu_r(norm_div(fertility))
plot_bar(
    df_2000, fertility,
    colors=colors_div,
    title="Diverging Color Scale",
    colorbar_label="Deviation from Mean Fertility",
    norm=norm_div,
    cmap="RdBu_r",
    filename="diverging.png"
)

