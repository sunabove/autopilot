# plot 4d scatter
# pip install numpy scipy mayavi PyQt5

import numpy as np
from scipy import stats
from mayavi import mlab

mu, sigma = 0, 0.1 
x = 10*np.random.normal(mu, sigma, 5000)
y = 10*np.random.normal(mu, sigma, 5000)
z = 10*np.random.normal(mu, sigma, 5000)

xyz = np.vstack([x,y,z])
kde = stats.gaussian_kde(xyz)
density = kde(xyz) 

x = [ 0, 1, 2, 3 ]
x = [ 0, 1, 2, 3 ]
x = [ 0, 1, 2, 3 ]
density = [ 0.2, 0.5, 0.7 ] 

# Plot scatter with mayavi
figure = mlab.figure('DensityPlot')
pts = mlab.points3d(x, y, z, density, scale_mode='none', scale_factor=0.07)
mlab.axes()
mlab.show()