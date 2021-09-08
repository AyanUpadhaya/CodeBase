# Matplotlib Subplots

#Display Multiple Plots

import matplotlib.pyplot as plt

import numpy as np



#plot1

x= np.array([0,1,2,3])
y= np.array([3,8,1,10])

plt.subplot(2,3,1)
plt.plot(x,y)
plt.title('Main Charts')

#plot2

x= np.array([0,1,2,3])
y= np.array([10,20,30,40])

plt.subplot(2,3,2)
plt.plot(x,y)

plt.title('Line Charts')

#plot3

x= np.array([1,2,3,4])
y= np.array([10,20,30,40])

plt.subplot(2,3,3)
plt.plot(x,y)




plt.show()

"""
The subplot() function takes three arguments that describes layout
The layout is organized in rows and columns, which are represented by the first and second argument.

The third argument represents the index of the current plot.
"""
