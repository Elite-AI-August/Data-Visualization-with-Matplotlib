import numpy as np
import matplotlib.pyplot as plt

# generate data
x = np.random.rand(1, 30)
y = np.random.rand(1, 30)

# configure and plot
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.set_title('Scatter Plot')
plt.xlabel('X')
plt.ylabel('Y')
ax1.scatter(x,y, c='r', marker='o') # scatter plot
plt.legend('x1')
plt.savefig("scatter_plot.png")
plt.show()
