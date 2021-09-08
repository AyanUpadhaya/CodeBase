import matplotlib.pyplot as plt
import numpy as np

y = np.array([50,80,75,25])

mylabels = ['facebook','youtube','programming','twitter']
myexplode = [0,0.2,0,0]

plt.pie(y,labels = mylabels,explode = myexplode, shadow = True)

plt.title('Activities')
# ~ plt.legend()
plt.show()
