import numpy as np
import matplotlib.pyplot as plt

def rootytoot(coeff, degree):
        from itertools import product
        realy = list()
        imagy = list()
        for coeffs in product(coeff,repeat=degree):
                rootie = np.roots(coeffs)
                for rooter in list(rootie):
                        if rooter.imag < 0 and 0 <= rooter.real:
                                realy.append(rooter.real)
                                imagy.append(rooter.imag)
        return [realy,imagy]
        
[realy,imagy]=rootytoot([1, -1], 25)

def histogrammar(realy, imagy, colormaps, bins, dpi):
    H, xedges, yedges = np.histogram2d(imagy, realy, bins=bins)
    H = np.log1p( H )
    extent = [yedges[0], yedges[-1], xedges[-1], xedges[0]]
    if colormaps == 'all':
        colormaps=[m for m in plt.cm.datad]
    for i, colormap in enumerate(colormaps):
        fig=plt.figure( frameon=False)
        ax=fig.gca()
        ax.axis('off')
        #fig.patch.set_visible(False)
        plt.setp(ax, frame_on=True)
        plt.setp(ax.get_xticklabels(), visible=False)
        plt.setp(ax.get_yticklabels(), visible=False)
        plt.setp(ax.get_xticklines(), visible=False)
        plt.setp(ax.get_yticklines(), visible=False)
        plt.imshow(H,interpolation='bicubic',extent=extent, cmap=plt.cm.get_cmap(colormap) )
        plt.savefig('roots' + str(bins) + colormap + '.png',dpi=dpi, facecolor='w', edgecolor='w', bbox_inches='tight', pad_inches=0)
        plt.close(fig)

histogrammar(realy, imagy, ['GnBu', 'Greys','Greys_r','gray','gray_r','ocean','terrain'], 1200, 600)
