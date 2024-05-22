import matplotlib.pyplot as plt
import numpy as np

#You can use the keyword argument markersize or the shorter version, ms

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20)
plt.show()