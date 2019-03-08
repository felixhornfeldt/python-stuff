import matplotlib.pyplot as plt

start_values = [i for i in range(10)]
squares = [i**2 for i in range(10)]

plt.plot(start_values, squares, linewidth=5)

plt.title("Squares from 1-10", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

plt.tick_params(axis='both', labelsize=8)

plt.show()

