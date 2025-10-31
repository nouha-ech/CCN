import numpy.random as rd
import matplotlib.pyplot as plt

n_simulations = 10000
data = rd.randint(0, 6, 10000)  

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.hist(data, bins=range(7), edgecolor='k', color='steelblue', density=False)
ax1.set_xlabel('Valeur')
ax1.set_ylabel('Fréquence')
ax1.grid(axis='y', alpha=0.3)

ax2.hist(data, bins=range(7), edgecolor='k', color='steelblue', density=True)
ax2.set_xlabel('Valeur')
ax2.set_ylabel('Fréquence relative')
ax2.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.show()

