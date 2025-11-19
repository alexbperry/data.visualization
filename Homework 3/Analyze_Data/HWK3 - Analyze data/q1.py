import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('scores.csv')

scores = df['Score']

plt.figure(figsize=(15, 4))

plt.subplot(1, 3, 1)
plt.hist(scores, bins=50, color='skyblue', edgecolor='black')
plt.title("Too Peaky (bins=50)")
plt.xlabel("Score")
plt.ylabel("Frequency")

plt.subplot(1, 3, 2)
plt.hist(scores, bins=5, color='salmon', edgecolor='black')
plt.title("Too Smooth (bins=5)")
plt.xlabel("Score")

bins = 15  

plt.subplot(1, 3, 3)
plt.hist(scores, bins=bins, color='lightgreen', edgecolor='black')
plt.title(f"Just Right (bins={bins})")
plt.xlabel("Score")


plt.subplot(1, 3, 3)
plt.hist(scores, bins=bins, color='lightgreen', edgecolor='black')
plt.title(f"Just Right (bins={bins})")
plt.xlabel("Score")

plt.tight_layout()
plt.savefig('q1.png', dpi=300, bbox_inches='tight')
plt.show()
