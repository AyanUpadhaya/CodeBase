# Matplotlib Scatter

# scatter() function to draw scatter plot

import matplotlib.pyplot as plt

import numpy as np

xaxis = np.array([5,7,8,7,2,18,2,9,4,11,12,6,9])

yaxis = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

colors = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])

# ~ plt.scatter(xaxis,yaxis)

sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])

plt.scatter(xaxis, yaxis, s=sizes,color = colors,cmap='viridis',alpha=0.5)

plt.colorbar()
plt.show()
