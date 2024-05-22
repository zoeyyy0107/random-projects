import matplotlib.pyplot as plt
import numpy as np

#You can use the keyword argument linestyle, or shorter ls
"""
'solid' (default) 	'-' 	
'dotted' 	        ':' 	
'dashed' 	        '--' 	
'dashdot' 	        '-.'
"""
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linestyle = 'dotted')
plt.show()