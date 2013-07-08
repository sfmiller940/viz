#
# Basic functions for viewing dynamics of the shifted sine function
#


twopi = 2 * math.pi
# Define the function that we'll be iterating.
def sinu(X,Y):
    return ( 0.5 + ( 0.5 * math.sin( twopi * ( X - Y ) ) ) )

#Make dynamic sine wave
def dynsine( mincomp, maxcomp, npoints, Xshift, Ymin, Ymax, bins, dpi, colormaps):
    Xs = list()
    Ys = list()
    #Pick random points, iterate sinu on them and store resulting points in a list.
    for npoint in range(npoints):
        X = random.random()
        Y = Ymin + ( random.random() * ( Ymax - Ymin ) )
        for comp in range(mincomp):
            X = sinu(X,Y)
        for comp in range(mincomp, maxcomp):
            X = sinu(X,Y)
            Xs.append( ( X + Xshift ) % 1  )
            Ys.append( Y )
    # Make histogram of points
    Hist, Xedges, Yedges = histogram2d( Xs, Ys, bins=bins)
    Hist = np.log1p(  Hist )
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
        imshow(Hist, interpolation='bicubic', cmap=cm.get_cmap(colormap), origin='lower', extent=[-3.14,3.14,-1,1])
        f80.savefig('sineprint_' + colormap + '.png',dpi=dpi, facecolor='w', edgecolor='w', bbox_inches='tight')
        close( f80 )


#Example
dynsine(15,40,1000000,0,0.265,1.265,1000,1000, ['bone','gist_ncar_r','Accent','afmhot'])