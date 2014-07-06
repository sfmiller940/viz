# rootytoot( coeff = list() ) returns the roots [comrealy,comimagy] of degree 18 polynomials with coeffs = [a,b,c] minus the strictly real roots Im(z)=0 .
# This can take a while. You might want to lower the degree for test runs.
def rootytoot(coeff, degree):
        from itertools import product
        realy = list()
        imagy = list()
        for coeffs in product(coeff,repeat=degree):
                rootie = roots(coeffs)
                for rooter in list(rootie):
                        if rooter.imag < 0 and 0 <= rooter.real:
                                realy.append(rooter.real)
                                imagy.append(rooter.imag)
        return [realy,imagy]

def histogrammar(realy, imagy, colormaps, bins, dpi):
    H, xedges, yedges = histogram2d(imagy, realy, bins=bins)
    H = np.log1p( H )
    extent = [yedges[0], yedges[-1], xedges[-1], xedges[0]]
    if colormaps == 'all':
        colormaps=[m for m in cm.datad]
    for i, colormap in enumerate(colormaps):
        fig=figure( facecolor='w', edgecolor='w')
        ax=gca()
        setp(ax, frame_on=True)
        setp(ax.get_xticklabels(), visible=False)
        setp(ax.get_yticklabels(), visible=False)
        setp(ax.get_xticklines(), visible=False)
        setp(ax.get_yticklines(), visible=False)
        imshow(H,interpolation='bicubic',extent=extent, cmap=cm.get_cmap(colormap) )
        savefig('roots' + str(bins) + colormap + '.png',dpi=dpi, facecolor='w', edgecolor='w', bbox_inches='tight')
        close(fig)

#Create Data
[realy,imagy]=rootytoot([1, 0.0+1.0j], 17)

#View Data
histogrammar(realy, imagy, ['hot', 'RdBu'], 700, 300)



#Make stills for given coeffs of given degree w/ every colormap
def rootstills( coeff, degree, bins, dpi):
  import matplotlib as mpl
  import numpy as np
  from itertools import product
	realy = list()
	imagy = list()
	for group in product( coeff , repeat=degree):
		rootie = roots(group)
		for rooter in list(rootie):
			if ( rooter.imag < 0 ) and ( rooter.real > 0 ):
				realy.append(rooter.real)
				imagy.append(rooter.imag)
	H, xedges, yedges = histogram2d(imagy,realy, bins=bins)
	H = np.log1p( H  )
	extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
	maps=[m for m in cm.datad]
	maps.sort()
	for colormap in maps:
		fig=figure( facecolor='w', edgecolor='w')
		ax=gca()
		setp(ax, frame_on=True)
		setp(ax.get_xticklabels(), visible=False)
		setp(ax.get_yticklabels(), visible=False)
		setp(ax.get_xticklines(), visible=False)
		setp(ax.get_yticklines(), visible=False)
		imshow(H,interpolation='bicubic',extent=extent, cmap=get_cmap(colormap) )
		savefig('rootstill2' + colormap + '.png',dpi=dpi, facecolor='w', edgecolor='w', bbox_inches='tight')
		ax.clear()
		close(fig)
