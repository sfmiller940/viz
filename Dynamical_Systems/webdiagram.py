def webby(nsteps, npaths, start, delta, bg):
        import numpy as np
        import matplotlib.path as mpath
        import matplotlib.patches as mpatches
        import matplotlib.pyplot as plt
        import random


        fig = plt.figure()
        ax = fig.add_subplot(111, axisbg=bg)

        X1 = np.arange(-2.7, 2.7, 0.1);
        ax.plot(X1,X1,color='r', lw=3.0)
        Y1 = X1 ** 3 - 3 * X1
        ax.plot(X1, Y1, color='r', lw=3.0)

        for j in range(npaths):
                X=[start + j * delta ]
                Y=[start + j * delta ]  
                for i in range(nsteps):
                        X.append(X[i])
                        Y.append(X[i] * X[i] * X[i] - 3 * X[i])
                        X.append(Y[i+1])
                        Y.append(Y[i+1])
                color = str( 1.0 - (j / npaths)  )
                ax.plot(X,Y, color=color, lw=2.0)
        plt.xlim(-2.5, 2.5)
        plt.ylim(-2.5, 2.5)
        plt.show()

#Example
webby(5,90,-2.05, 0.01)

