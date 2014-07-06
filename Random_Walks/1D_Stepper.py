# 1D Basic Random Walk
def randomwalks(nsteps,nwalks):
        import matplotlib.pyplot as plt
        import random
        for j in range(nwalks):
                X = [0]
                for i in range(nsteps):
                        X.append(  X[i] + random.choice([-1,1]) )
                plt.plot(X)
        X=[0]          
        for i in range(nsteps):
                X.append(0)
        plt.plot(X, color='k', linewidth=2.0)
        return X
