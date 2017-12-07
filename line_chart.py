import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1,11)
values = np.random.rand(10)

plt.plot(x,values)

plt.xlabel('ith Iteration')
plt.ylabel('Random VariabLE')
plt.show()
plt.close()