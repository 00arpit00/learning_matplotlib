import matplotlib.pyplot as plt
import numpy as np

names = list('abcdefghij')
a = np.random.rand(10,10)
plt.matshow(a)
plt.xticks(np.arange(10),names)
plt.yticks(np.arange(10),names)
plt.show()