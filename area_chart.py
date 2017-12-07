import matplotlib.pyplot as plt
import numpy as np


x = np.array(range(1,11))
y = [1,2,3,4,5,6,7,8,9,10]

plt.fill_between(x,0,y[::-1])
plt.show()