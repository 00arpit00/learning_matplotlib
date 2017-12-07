import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1,11)
y1 = x+5
y2 = x**2

plt.plot(x,y1)
plt.plot(x,y2)

plt.xlabel('ith Iteration')
plt.ylabel('Random VariabLE')
plt.show()
plt.close()