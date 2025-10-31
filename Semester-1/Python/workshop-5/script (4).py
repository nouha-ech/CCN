import matplotlib.pyplot as plt

x_vertices = [0.5, 1.0, 3.0, 3.5, 2.0]
y_vertices = [2.0, 0.0, 0.0, 2.0, 3.0]

order = [0, 2, 4, 1, 3, 0]
x_star = [x_vertices[i] for i in order]
y_star = [y_vertices[i] for i in order]
plt.figure(figsize=(6,5))
plt.plot(x_star, y_star) 
plt.grid(True)
plt.xlim(0.4, 3.6)
plt.ylim(-0.2, 3.2)
plt.xlabel("x")
plt.ylabel("y")
plt.show()


