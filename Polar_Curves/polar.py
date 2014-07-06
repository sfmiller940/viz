# I forget what these functions do, but I'll build on this and straighten it out.
# More info here: http://matplotlib.sourceforge.net/examples/pylab_examples/polar_demo.html

def param(nsteps):
        import numpy as np
        import matplotlib.path as mpath
        import matplotlib.patches as mpatches
        import matplotlib.pyplot as plt
        import random

        Path = mpath.Path

        fig = plt.figure()
        ax = fig.add_subplot(111)

        T = np.linspace(0, 2 * np.pi, nsteps)
        for pq in range(0,23):
                for rs in range(0,23):
                        X = np.cos( (23 - pq) * T)
                        Y = np.sin( (23 - rs) * T)
                        pathdata = [ (Path.MOVETO, (X[0], Y[0]))]
                        for i in range(nsteps-1):
                                pathdata.append( (Path.LINETO, (X[i+1],Y[i+1]) ) )
                        codes, verts = zip(*pathdata)
                        path = mpath.Path(verts, codes)
                        x, y = zip(*path.vertices)
                        line, = ax.plot(x, y, linewidth=3.0)
        plt.show()


def polar():
        import matplotlib
        import numpy as np
        from matplotlib.pyplot import figure, show, rc, grid

        fig = figure()
        ax = fig.add_axes([0.1, 0.1, 0.8, 0.8],polar=True)

        theta = np.arange(0, 2 * np.pi , 0.01)
        for pq in range(1,24):
                for rs in range (1,24):
                        r = np.sin(pq * theta) + np.cos(rs * theta)
                        ax.plot(theta, r, linewidth=2.0)
        show()

# sweet loops
def polar(nloops, max, delta):
        import matplotlib
        import numpy as np
        from matplotlib.pyplot import figure, show, rc, grid
        rc('grid', color='#316931', linewidth=0, linestyle='-')
        rc('xtick', labelsize=0)
        rc('ytick', labelsize=0)

        fig = figure()
        ax = fig.add_axes([0.1, 0.1, 0.8, 0.8],polar=True, axisbg='k')

        theta = np.arange(0, 2 * np.pi , 0.001)
        for rs in range (1,nloops):
                r = np.sin(( nloops - rs ) * theta) * (max - rs / delta) )
                ax.plot(theta, r, linewidth=4.0)
        show()



# Example. It's important that delta have a decimal or division is floored.
polar(36,10,5.0)
