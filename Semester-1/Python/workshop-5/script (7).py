import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(12, 10))
ax.set_xlim(-8, 8)
ax.set_ylim(-4, 10)
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)
ax.axhline(y=0, color='k', linewidth=0.5)
ax.axvline(x=0, color='k', linewidth=0.5)
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y', fontsize=12)
ax.set_title('Graphiques des fonctions f₁ à f₇', fontsize=14, fontweight='bold')

x1a = np.linspace(3, 10, 200)
y1a = 3 * np.sqrt(1 - x1a**2 / 49)
ax.plot(x1a, y1a, color='#e63946', linewidth=2, label='f₁')
x1b = np.linspace(-10, -3, 200)
y1b = 3 * np.sqrt(1 - x1b**2 / 49)
ax.plot(x1b, y1b, color='#e63946', linewidth=2)

x2a = np.linspace(4, 10, 200)
y2a = -3 * np.sqrt(1 - x2a**2 / 49)
ax.plot(x2a, y2a, color='#f77f00', linewidth=2, label='f₂')

x2b = np.linspace(-10, -4, 200)
y2b = -3 * np.sqrt(1 - x2b**2 / 49)
ax.plot(x2b, y2b, color='#f77f00', linewidth=2)

x3a = np.linspace(0.75,4, 100)
y3a = 9 - 8 * np.abs(x3a)
ax.plot(x3a, y3a, color='#06d6a0', linewidth=2, label='f₃')

x3b = np.linspace(-4, -0.75, 100)
y3b = 9 - 8 * np.abs(x3b)
ax.plot(x3b, y3b, color='#06d6a0', linewidth=2)

x4a = np.linspace(-1, 1, 100)
y4a = 0.75 + 3 * np.abs(x4a)
ax.plot(x4a, y4a, color='#118ab2', linewidth=2, label='f₄')

x4b = np.linspace(-1, 1, 100)
y4b = 0.75 + 3 * np.abs(x4b)
ax.plot(x4b, y4b, color='#118ab2', linewidth=2)

x5 = np.linspace(-1, 1, 100)
y5 = np.full_like(x5, 2.25)
ax.plot(x5, y5, color='#073b4c', linewidth=2, label='f₅')

x6 = np.linspace(-4, 4, 1000)
term1 = np.abs(x6) / 2
term2 = (3 * np.sqrt(33) / 112) * x6**2
term3_arg = 1 - (np.abs(np.abs(x6) - 2) - 1)**2
term3_arg = np.maximum(term3_arg, 0)  
term3 = np.sqrt(term3_arg)
y6 = term1 - term2 + term3 - 3
ax.plot(x6, y6, color='#8338ec', linewidth=2, label='f₆')

sqrt10 = np.sqrt(10)

x7a = np.linspace(-3, -1, 200)
term1_7a = 6 * sqrt10 / 7
term2_7a = 1.5 - 0.5 * np.abs(x7a)
term3_arg_7a = 3 + 2 * np.abs(x7a) - x7a**2
term3_arg_7a = np.maximum(term3_arg_7a, 0)
term3_7a = (6 * sqrt10 / 14) * np.sqrt(term3_arg_7a)
y7a = term1_7a + term2_7a - term3_7a
ax.plot(x7a, y7a, color='#ff006e', linewidth=2, label='f₇')

x7b = np.linspace(1, 3, 200)
term1_7b = 6 * sqrt10 / 7
term2_7b = 1.5 - 0.5 * np.abs(x7b)
term3_arg_7b = 3 + 2 * np.abs(x7b) - x7b**2
term3_arg_7b = np.maximum(term3_arg_7b, 0)
term3_7b = (6 * sqrt10 / 14) * np.sqrt(term3_arg_7b)
y7b = term1_7b + term2_7b - term3_7b
ax.plot(x7b, y7b, color='#ff006e', linewidth=2)

ax.legend(loc='upper right', fontsize=10)

plt.tight_layout()
plt.show()