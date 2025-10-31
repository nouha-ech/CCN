import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(0)
n = 200
A = np.random.normal(loc=0, scale=1, size=n)
B = 0.1*A + np.random.normal(0, 0.8, size=n)
C = np.random.normal(0, 1, size=n)
D = -0.5*A + 0.3*C + np.random.normal(0, 0.6, size=n)
E = 0.2*B + 0.8*np.random.normal(0, 1, size=n)

df = pd.DataFrame({'A': A, 'B': B, 'C': C, 'D': D, 'E': E})
corr = df.corr()

fig, ax = plt.subplots(figsize=(7,6))
im = ax.imshow(corr, cmap='coolwarm', vmin=-1, vmax=1)

for i in range(len(corr)):
    for j in range(len(corr)):
        ax.text(j, i, f"{corr.iloc[i, j]:.2f}",
                ha='center', va='center', color='black', fontsize=9)

ax.set_xticks(np.arange(len(corr.columns)))
ax.set_yticks(np.arange(len(corr.columns)))
ax.set_xticklabels(corr.columns)
ax.set_yticklabels(corr.columns)
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

plt.colorbar(im, shrink=0.8)
plt.tight_layout()
plt.show()

