#Matplotlib Bars

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["Facebook","Youtube","Programming","Twitter"])
y = np.array([50,80,75,25])

# ~ plt.bar(x,y)
# ~ plt.bar(x,y,color=colors)

colors =np.array(['blue','red','orange','aqua'])

plt.bar(x,y,color=colors,width = 0.5)


# ~ plt.barh(x, y, height = 0.1) for bar horizonatal

plt.title('Ayan\'s Acitvities')
plt.show()
