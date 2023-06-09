import matplotlib.pyplot as plt

x_value = list(range(1, 1001))
y_value = [x**2 for x in x_value]

plt.scatter(x_value, y_value, c=y_value, cmap=plt.cm.Blues, edgecolor='none', s = 40)
plt.title("Square Numbers", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of Value", fontsize = 14)
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
