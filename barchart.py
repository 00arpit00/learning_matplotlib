import matplotlib.pyplot as plt
import numpy as np

x = np.arange(10)
values = np.random.randint(1,100,10)
names = list('ABCEDEFGHI')

plt.bar(x,values,align='center')
plt.xticks(x,names)
plt.ylabel('Random Variable')
plt.show()