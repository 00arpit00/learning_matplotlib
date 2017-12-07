import matplotlib.pyplot as plt
import numpy as np

labels = list('ABED')

sizes = [100,250,300,400]
explode = [.1,0,0,0]
plt.pie(sizes, explode=explode,labels=labels)
plt.show()