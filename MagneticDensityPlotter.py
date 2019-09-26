# plot 4d scatter
# pip install numpy scipy mayavi PyQt5

import numpy as np
from scipy import stats
from mayavi import mlab

import pandas as pd

df = pd.read_excel ( r'magnetic_density_data.xlsx')
#(use "r" before the path string to address special character, such as '\').
# Don't forget to put the file name at the end of the path + '.xlsx'

x = df[ 'x' ].tolist()
y = df[ 'y' ].tolist()
z = df[ 'z' ].tolist()
v = df[ 'value' ].tolist()

''' 
x = [ 1, 1, 1, 1 ]
y = [ 1, 2, 2, 3 ]
z = [ 1, 2, 1, 3 ]
v = [ .3, .4, .5, .2 ]
'''

# Plot scatter with mayavi
figure = mlab.figure( 'Magnetic Field Density' )
sf = 0.07
sf = 1
pts = mlab.points3d(x, y, z, v, scale_mode='none', scale_factor=sf)

mlab.axes()
mlab.show()