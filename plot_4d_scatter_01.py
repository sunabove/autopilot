# plot 4d scatter
# pip install numpy scipy mayavi PyQt5

from mpl_toolkits import mplot3d

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.axes(projection="3d") 

x = [ 1, 2, 3 ]
y = [ 4, 5, 6 ]
z = [ 7, 8, 9 ]
density = [ 0.2, 0.5, 0.7 ]

ax.scatter3D(x, y, z, c=density, cmap='hsv');

plt.show()