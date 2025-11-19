import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('scores.csv')

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

df.boxplot(column='Score', by='Major', ax=axes[0,0])
axes[0,0].set_title('Score by Major')
axes[0,0].set_xlabel('Major')
axes[0,0].set_ylabel('Score')

df.boxplot(column='Score', by='Semester', ax=axes[0,1])
axes[0,1].set_title('Score by Semester')
axes[0,1].set_xlabel('Semester')
axes[0,1].set_ylabel('Score')

df.boxplot(column='Score', by='Student type', ax=axes[1,0])
axes[1,0].set_title('Score by Student type')
axes[1,0].set_xlabel('Student type')
axes[1,0].set_ylabel('Score')

df.boxplot(column='Score', by='Sex', ax=axes[1,1])
axes[1,1].set_title('Score by Sex')
axes[1,1].set_xlabel('Sex')
axes[1,1].set_ylabel('Score')

plt.suptitle('')
plt.tight_layout()
plt.savefig('q3.png')
plt.show()



