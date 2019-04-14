import numpy as np 
import matplotlib.pyplot as plt 

# data 
x1 = np.linspace(0.0, 5.0)
x2 = np.linspace(0.0, 2.0)
y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
y2 = np.cos(2 * np.pi * x2)

# specification of subplot 1
plt.subplot(2, 1, 1)
plt.plot(x1, y1, 'o-')
plt.title('A table of 2 subplots')
plt.ylabel('Damped oscillation')

# specification of subplot 2
plt.subplot(2, 1, 2)
plt.plot(x2, y2, '.-')
plt.xlabel('times (s)')
plt.ylabel('Undamped oscillation')

# show the plot
plt.savefig("subplots.png")
plt.show()