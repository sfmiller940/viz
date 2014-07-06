# 2D NSEW Directions
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
                        dir = random.choice([1,2,3,4])
                        if dir == 1:
                                Y=Y+1
                        elif dir == 2:
                                X=X+1
                        elif dir == 3:
                                Y=Y-1
                        elif dir == 4:
                                X=X-1
                        pathdata.append( (Path.LINETO, (X,Y) ) )
                codes, verts = zip(*pathdata)
                path = mpath.Path(verts, codes)
                x, y = zip(*path.vertices)
                line, = ax.plot(x, y, linewidth=2.0)
        plt.show()
