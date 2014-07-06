#
# Standard Map Movie Maker
#
def standardmov( mincomp, maxcomp, res, nrandom, bins, Tmin, Tmax, nframes, fname, colormaps):
        import random
        import matplotlib as mpl
        import numpy as np
        twopi = 2 * math.pi
        pitwo = 2 / math.pi
        X0 = np.arange( 0 , 1 , res )
        Y0 = np.arange( 0, 1 , res )
        X0,Y0 = np.meshgrid(X0,Y0)
	#Main loop to make the individual images of the movie.
        for frame in range(nframes+1):
                xpts = list()
                ypts = list()
                X,Y = X0,Y0
                T = Tmin + ( 1.0 * ( Tmax - Tmin ) * frame / nframes )
                gamma = 0.48 * pitwo * np.arcsin( T )
                delta = -0.5 + ( 2.0 * T )
                sindelta =  math.sin( T * math.pi )
		# Define the function being used this frame
                def F(X, Y):
                        X = ( X + ( gamma * np.sin( Y * twopi ) ) ) % 1
                        return[ X , ( X + Y ) % 1 ]
		# Iterate function on the mesh.
                for k in range(mincomp):
                        X, Y = F( X, Y )
                for k in range(mincomp,maxcomp):
                        X, Y = F( X, Y )
                        xpts.extend( ( ( X + sindelta ) % 1 ).ravel() )
                        ypts.extend( ((Y + delta) % 1 ).ravel() )
		# Iterate function on random points
                for j in range(nrandom):
                        X = random.random()
                        Y = random.random()
                        for k in range(mincomp):
                                X, Y = F( X, Y )
                        for k in range(mincomp,maxcomp):
                                X, Y = F( X, Y )
                                xpts.append( ( X + sindelta ) % 1 )
                                ypts.append( (Y + delta) % 1  )
                # Make histogram of points
                H, xedges, yedges = histogram2d(xpts, ypts, bins=bins)
                H = np.log1p( H )
                # Make an image for each colormap
                for i, colormap in enumerate(colormaps):
                        f80 = figure( facecolor='w', edgecolor='w')
                        #f80.set_size_inches(18,12)
                        ax=gca()
                        setp(ax, frame_on=True)
                        setp(ax.get_xticklabels(), visible=False)
                        setp(ax.get_yticklabels(), visible=False)
                        setp(ax.get_xticklines(), visible=False)
                        setp(ax.get_yticklines(), visible=False)
                        imshow(H, interpolation='bicubic', cmap=cm.get_cmap(colormap), origin='lower', extent=[-6.4,6.4,-4,4])
                        filename = fname + colormap
                        if frame < 10: filename += '000'
                        elif frame < 100: filename += '00'
                        elif frame < 1000: filename += '0'
                        f80.savefig(filename + str(frame) + '.png',dpi=250, facecolor='w', edgecolor='w', bbox_inches='tight')
                        close( f80 )
                print frame,

# Example
standardmov(50, 800, .02 , 1500 , 1250, 0.0, 1.0 , 1000, 'stdarc', ['jet','jet_r','Spectral_r'])
