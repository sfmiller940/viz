import math as math
import numpy as np
import random
import matplotlib.pyplot as plt

#
# Basic functions for viewing dynamics of the shifted sine function
#

twopi = 2 * math.pi

def sinu(X,Y):
    return ( 0.5 + ( 0.5 * math.sin( twopi * ( X - Y ) ) ) )

#Make dynamic sine wave
def dynsine( mincomp, maxcomp, npoints, Xshift, Ymin, Ymax):
    Xs = list()
    Ys = list()
    for npoint in range(npoints):
        if npoint % 1000 == 0:
            print (npoint)
        X = random.random()
        Y = Ymin + ( random.random() * ( Ymax - Ymin ) )
        for comp in range(mincomp):
            X = sinu(X,Y)
        for comp in range(mincomp, maxcomp):
            X = sinu(X,Y)
            Xs.append( ( X + Xshift ) % 1  )
            Ys.append( Y )
    return Xs, Ys

#Xs, Ys = dynsine(15,40,20000000,0,0.265,1.265)    
    
def histogrammar(dpi, colormaps):    
    Hist, Xedges, Yedges = np.histogram2d( Xs, Ys, bins=(9360, 3000))
    Hist = np.log1p(  Hist )
    # Make an image for each colormap
    # colormaps = [m for m in cm.datad]
    # colormaps.sort()
    for i, colormap in enumerate(colormaps):
        f80 = plt.figure(frameon=False)
        #f80.set_size_inches(18,12)
        ax=f80.gca()
        ax.axis('off')
        plt.setp(ax, frame_on=True)
        plt.setp(ax.get_xticklabels(), visible=False)
        plt.setp(ax.get_yticklabels(), visible=False)
        plt.setp(ax.get_xticklines(), visible=False)
        plt.setp(ax.get_yticklines(), visible=False)
        plt.imshow(Hist, interpolation='bicubic', cmap=plt.cm.get_cmap(colormap), origin='lower', extent=[-3.14,3.14,-1,1])
        f80.savefig('sineprint_' + colormap + '.png',dpi=dpi, facecolor='w', edgecolor='w', bbox_inches='tight', pad_inches=0)
        plt.close( f80 )


#Example
histogrammar(2500, ['Greys', 'gray_r','bone','gist_ncar_r','Accent','afmhot','binary','cubehelix','gist_rainbow_r','hsv_r','ocean_r','seismic','Set1','Set3','terrain_r','YlGnBu'])
