import matplotlib.pyplot as plt

x_points = [0.5, 1.0, 2.0, 3.0, 3.5]
y_points = [2.0, 0.0, 3.0, 0.0, 2.0]
order = [0, 2, 4, 3, 1, 0]
x_pentagon = [x_points[i] for i in order]
y_pentagon = [y_points[i] for i in order]

plt.figure(figsize=(6,5))
plt.plot(x_pentagon, y_pentagon)
plt.grid(True)
plt.xlim(0.4, 3.6)
plt.ylim(-0.2, 3.2)
plt.xticks([0.5, 1.0, 2.0, 3.0, 3.5])
plt.yticks([0, 0.5, 1, 1.5, 2, 2.5, 3])
plt.xlabel("x")
plt.ylabel("y")
plt.show()
