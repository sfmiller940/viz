#Basic function for making movies.
def rootytoot(numframes,colormap):
        realy = list()
        imagy = list()
        from itertools import product
        f80 = figure( facecolor='k', edgecolor='k')
        for frame in range(numframes + 1):
               theta = math.pi - ( ( frame * math.pi ) / ( 2 * numframes) )
               coeff=[1, math.cos( theta ) + ( math.sin( theta ) * (0.0+1.0j))  ]
               for a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15 in product(coeff,repeat=15):
                        rootie = roots([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15])
                        for rooter in list(rootie):
                                realy.append(rooter.real)
                                imagy.append(rooter.imag)
               H, xedges, yedges = histogram2d(imagy, realy, bins=(300,300))
               extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
               imshow(H,interpolation='bicubic', extent=extent, cmap=colormap)
               f80.savefig('roots' + str(frame) + '.png',dpi=200, facecolor='k', edgecolor='k')
