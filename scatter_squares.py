import matplotlib.pyplot as plt
from matplotlib import ticker


x_values = range(1, 1001)
y_values = [x**2 for x in x_values]


plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# set title + label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# set range for each axis
ax.axis([0, 1100, 0, 1100000])

# turn scientific notation off 
formatter = ticker.ScalarFormatter()
formatter.set_scientific(False)
ax.yaxis.set_major_formatter(formatter)
fig.tight_layout()

plt.show()
#plt.savefig('squares_plot.png', bbox_inches='tight')