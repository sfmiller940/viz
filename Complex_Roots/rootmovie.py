import math as math
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from itertools import product

#The main function that makes the frames for the movie
def rootmov( numframes, degree, bins, dpi):
        #Main loop for making frame images
        for frame in range(1,numframes + 1):
               realy = list()
               imagy = list()
               percent = 1.0 * frame / numframes
               # Find the roots of all polynomials of given degree as coefficients vary.
	       for group in product(pathcoeff(percent),repeat=degree):
                        rootie = np.roots(group)
                        for rooter in list(rootie):
                                if rooter.imag != 0:
                                        realy.append(rooter.real)
                                        imagy.append(- rooter.imag)
               # Make histogram of roots.
               H, xedges, yedges = np.histogram2d(realy,imagy, bins=bins)
               H = np.log1p( 1 / (1 + H ) )
               # Configure and save an image of the histogram.
               fig=plt.figure( facecolor='k', edgecolor='k')
               ax=plt.gca()
               plt.setp(ax, frame_on=True)
               plt.setp(ax.get_xticklabels(), visible=False)
               plt.setp(ax.get_yticklabels(), visible=False)
               plt.setp(ax.get_xticklines(), visible=False)
               plt.setp(ax.get_yticklines(), visible=False)
               plt.imshow(H,interpolation='bicubic',extent=[0,1000,0,600], cmap=dynacm( percent ) )
               plt.savefig("root_test{:04}.png".format(frame),dpi=dpi, facecolor='k', edgecolor='k', bbox_inches='tight')
               ax.clear()
               plt.close(fig)
	       

# Trace a path of coefficients in the complex plane.
def pathcoeff(percent):
	#The spiral from the origin to -1.
	if percent < 0.4 :
		percent = percent * 2.5
		T = 0.5 - ( 0.5 * math.cos ( percent * math.pi ) )
		R = T
		X = - R * math.cos ( T * 4 * math.pi )
		Y = R * math.sin( T * 4 * math.pi )
	#Spiral from -1 to 2
	elif percent < 0.6:
		percent = ( percent - 0.4 ) * 5
		T = 0.5 - ( 0.5 * math.cos ( percent * math.pi ) )
		R = 1 + T
		X = - R * math.cos ( T * math.pi )
		Y = R * math.sin( - T * math.pi )
	#Spiral from 2 to 1
	else:
		percent = ( percent - 0.6 ) * 2.5
		T = 0.5 - ( 0.5 * math.cos ( percent * math.pi ) )
		R = 1 - T
		X = 1 + ( R * math.cos ( T * 4 * math.pi ) )
		Y = R * math.sin( T * 4 * math.pi )
	return [ X + ( Y * (0.0+1.0j) ), 1]


# Returns smoothly shifting colormaps depending on the percentage.
def dynacm(percent):
	factor = 0.5 * np.cos( 5 * math.pi * percent  )
	alpha = 0.5 + factor
	beta = 0.5 - factor
	if percent < 0.2:
		perccm = {
        		'red': lambda x:   ( beta *  gfunc[30](1 - x)  ) + ( alpha * gfunc[7](1 - x) )  ,
        		'green': lambda x:   ( beta *  gfunc[31](1 - x) ) + ( alpha * gfunc[5](1 - x)  ) ,
        		'blue': lambda x:   ( beta * gfunc[32](1 - x) ) + ( alpha *  gfunc[15](1 - x) ) ,
		}
	elif percent < 0.4:
		perccm = {
        		'red': lambda x:   ( beta *  gfunc[30](1 - x)  ) + ( alpha * gfunc[33](1 - x) )  ,
        		'green': lambda x:   ( beta *  gfunc[31](1 - x) ) + ( alpha * gfunc[13](1 - x)  ) ,
        		'blue': lambda x:   ( beta * gfunc[32](1 - x) ) + ( alpha *  gfunc[10](1 - x) ) ,
		}
	elif percent < 0.6 :
		perccm = {
        		'red': lambda x:   ( beta *  gfunc[3](1 - x)  ) + ( alpha * gfunc[33](1 - x) )  ,
        		'green': lambda x:   ( beta *  gfunc[28](1 - x) ) + ( alpha * gfunc[13](1 - x)  ) ,
        		'blue': lambda x:   ( beta * gfunc[23](1 - x) ) + ( alpha *  gfunc[10](1 - x) ) ,
		}
	elif percent < 0.8:
		perccm = {
        		'red': lambda x:   ( beta *  gfunc[3](1 - x)  ) + ( alpha * gfunc[30](x) )  ,
        		'green': lambda x:   ( beta *  gfunc[28](1 - x) ) + ( alpha * gfunc[31](x)  ) ,
        		'blue': lambda x:   ( beta * gfunc[23](1 - x) ) + ( alpha *  gfunc[32](x) ) ,
		}
	else:
		perccm = {
				'red': lambda x:   ( beta *  gfunc[23](x)  ) + ( alpha * gfunc[30](x) )  ,
        		'green': lambda x:   ( beta *  gfunc[28](x) ) + ( alpha * gfunc[31](x)  ) ,
        		'blue': lambda x:   ( beta * gfunc[3](x) ) + ( alpha *  gfunc[32](x) ) ,
		}		
	return  matplotlib.colors.LinearSegmentedColormap('my_colormap',perccm,256)
	       

# The following functions are borrowed from the Python colormap library.
gfunc = {
        0: lambda x: 0,
        1: lambda x: 0.5,
        2: lambda x: 1,
        3: lambda x: x,
        4: lambda x: x**2,
        5: lambda x: x**3,
        6: lambda x: x**4,
        7: lambda x: np.sqrt(x),
        8: lambda x: np.sqrt(np.sqrt(x)),
        9: lambda x: np.sin(x * np.pi / 2),
        10: lambda x: np.cos(x * np.pi / 2),
        11: lambda x: np.abs(x - 0.5),
        12: lambda x: (2 * x - 1)**2,
        13: lambda x: np.sin(x * np.pi),
        14: lambda x: np.abs(np.cos(x * np.pi)),
        15: lambda x: np.sin(x * 2 * np.pi),
        16: lambda x: np.cos(x * 2 * np.pi),
        17: lambda x: np.abs(np.sin(x * 2 * np.pi)),
        18: lambda x: np.abs(np.cos(x * 2 * np.pi)),
        19: lambda x: np.abs(np.sin(x * 4 * np.pi)),
        20: lambda x: np.abs(np.cos(x * 4 * np.pi)),
        21: lambda x: 3 * x,
        22: lambda x: 3 * x - 1,
        23: lambda x: 3 * x - 2,
        24: lambda x: np.abs(3 * x - 1),
        25: lambda x: np.abs(3 * x - 2),
        26: lambda x: (3 * x - 1) / 2,
        27: lambda x: (3 * x - 2) / 2,
        28: lambda x: np.abs((3 * x  - 1) / 2),
        29: lambda x: np.abs((3 * x  - 2) / 2),
        30: lambda x: x / 0.32 - 0.78125,
        31: lambda x: 2 * x - 0.84,
        32: lambda x: gfunc32(x),
        33: lambda x: np.abs(2 * x - 0.5),
        34: lambda x: 2 * x,
        35: lambda x: 2 * x - 0.5,
        36: lambda x: 2 * x - 1.
}

def gfunc32(x):
    ret = np.zeros(len(x))
    m = (x < 0.25)
    ret[m] = 4 * x[m]
    m = (x >= 0.25) & (x < 0.92)
    ret[m] = -2 * x[m] + 1.84
    m = (x >= 0.92)
    ret[m] = x[m] / 0.08 - 11.5
    return ret
