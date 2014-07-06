# 2D Pseudo Brownian        
def random2d(nsteps, npaths):
        import numpy as np
        import matplotlib.path as mpath
        import matplotlib.patches as mpatches
        import matplotlib.pyplot as plt
        import random

        Path = mpath.Path

        fig = plt.figure()
        ax = fig.add_subplot(111)

        for j in range(npaths):
                X=0
                Y=0
                pathdata = [ (Path.MOVETO, (X, Y))]
                for i in range(nsteps):
                        dist = random.normalvariate(1,0.5)
                        dir = random.uniform(0, 2 * np.pi )
                        X = X + dist * np.cos(dir)
                        Y = Y + dist * np.sin(dir)
                        pathdata.append( (Path.LINETO, (X,Y) ) )
                codes, verts = zip(*pathdata)
                path = mpath.Path(verts, codes)
                x, y = zip(*path.vertices)
                line, = ax.plot(x, y, linewidth=2.0)
        plt.show()

# Spiced up brownian motion
def random2d(nsteps, npaths, radius, colormap):
        import numpy as np
        import matplotlib.path as mpath
        import matplotlib.patches as mpatches
        import matplotlib.pyplot as plt
        import random

        Path = mpath.Path

        fig = plt.figure()
        ax = fig.add_subplot(111)

        for j in range(npaths):
                R = uniform(0, radius)
                T = uniform(0, 2 * np.pi)
                X= R * np.cos(T)
                Y= R * np.sin(T)
                pathdata = [ (Path.MOVETO, (X, Y))]
                for i in range( nsteps ):
                        dist = random.normalvariate(1,0.5)
                        dir = random.uniform(0, 2 * np.pi )
                        X = X + dist * np.cos(dir)
                        Y = Y + dist * np.sin(dir)
                        pathdata.append( (Path.LINETO, (X,Y) ) )
                codes, verts = zip(*pathdata)
                path = mpath.Path(verts, codes)
                x, y = zip(*path.vertices)
                line, = ax.plot(x, y, linewidth=2.0, color=colormap( 1.0 * j / npaths ))

        fig.set_facecolor("#000000")
        fig.set_edgecolor("#000000")
        rcParams['axes.facecolor'] = 'k'
        rcParams['axes.edgecolor'] = 'k'
        plt.show()

random2d(600, 80, 50, cm.prism)
