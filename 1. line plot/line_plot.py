import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
time = np.arange(0.0, 2.0, 0.01)
voltage = 1 + np.sin(2 * np.pi * time)

# configure and plot
fig, ax = plt.subplots()
ax.plot(time, voltage)
ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='voltage vs time')
ax.grid()
fig.savefig("line-plot.png")
plt.show()