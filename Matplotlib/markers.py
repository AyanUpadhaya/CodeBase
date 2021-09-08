# ~ Matplotlib Markers
# https://www.w3schools.com/python/matplotlib_markers.asp
# you can use marker keyword argument

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1,2,6,8])
ypoints = np.array([3,6,8,10])

# ~ plt.plot(xpoints,ypoints,marker ='o')
plt.plot(xpoints,ypoints,'o--')
plt.plot(xpoints,ypoints,'or')
plt.show()

# ~ 'o'	Circle	
# ~ '*'	Star	
# ~ '.'	Point	
# ~ ','	Pixel	
# ~ 'x'	X	
# ~ 'X'	X (filled)	
# ~ '+'	Plus	
# ~ 'P'	Plus (filled)	
# ~ 's'	Square	
# ~ 'D'	Diamond	
# ~ 'd'	Diamond (thin)	
# ~ 'p'	Pentagon	
# ~ 'H'	Hexagon	
# ~ 'h'	Hexagon	
# ~ 'v'	Triangle Down	
# ~ '^'	Triangle Up	
# ~ '<'	Triangle Left	
# ~ '>'	Triangle Right	
# ~ '1'	Tri Down	
# ~ '2'	Tri Up	
# ~ '3'	Tri Left	
# ~ '4'	Tri Right	
# ~ '|'	Vline	
# ~ '_'	Hline
