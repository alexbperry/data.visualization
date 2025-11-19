import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('scores.csv')
scores = df['Score']

score_min, score_max = scores.min(), scores.max()

plt.figure(figsize=(15, 4))

plt.subplot(1, 3, 1)
sns.kdeplot(scores, bw_adjust=0.1, clip=(score_min, score_max), fill=True, color='skyblue')
plt.title("Too Peaky (bw=0.1)")
plt.xlabel("Score")
plt.ylabel("Density")

plt.subplot(1, 3, 2)
sns.kdeplot(scores, bw_adjust=2, clip=(score_min, score_max), fill=True, color='salmon')
plt.title("Too Smooth (bw=2)")
plt.xlabel("Score")

plt.subplot(1, 3, 3)
sns.kdeplot(scores, bw_adjust=0.5, clip=(score_min, score_max), fill=True, color='lightgreen')
plt.title("Just Right (bw=0.5)")
plt.xlabel("Score")

plt.tight_layout()
plt.savefig('q2.png', dpi=300, bbox_inches='tight')
plt.show()
