# Matplotlib Linestyle

import matplotlib.pyplot as plt
import numpy as np

xpoints= np.array([1,2,6,8])
ypoints= np.array([2,4,6,10])

# ~ plt.plot(xpoints,ypoints,linestyle ='dotted')

#line color
plt.plot(xpoints,ypoints,marker='o',color ='r',linestyle='dotted')

plt.show()
