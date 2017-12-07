import matplotlib.pyplot as plt
import numpy as np

names = list('qwerty')
y = np.arange(6)
scores = [1,2,3,4,5,6]
plt.barh(y,scores,align='center',alpha=.4)
plt.yticks(y,names)
plt.show()