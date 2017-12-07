import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(1000)
x = map(lambda t:t>0.5,x)
plt.hist(x)
plt.show()