import matplotlib.pyplot as plt
import numpy as np

#markeredgecolor or the shorter mec to set the color of the edge
#markerfacecolor or the shorter mfc to set the color inside the edge 

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r', mfc = 'r')
plt.show()