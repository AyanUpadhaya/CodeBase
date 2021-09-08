# matplotlib
import matplotlib

#print(matplotlib.__version__)

#pyplot

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1,8])
ypoints = np.array([3,300])

plt.plot(xpoints,ypoints)

plt.show()

#By default, the plot() function draws a line from point to point.

# ~ Parameter 1 is an array containing the points on the x-axis.

# ~ Parameter 2 is an array containing the points on the y-axis.
