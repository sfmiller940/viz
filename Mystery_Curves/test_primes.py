import matplotlib.pyplot as plt
import numpy as np
 
def saveit(alpha,beta,gamma):  
    f80 = plt.gcf()
    ax=f80.gca()
    ax.axis('off')
    ax.set_aspect('equal', 'datalim')
    ax.set_ylim([-1,1])
    ax.set_xlim([-1,1])
    plt.setp(ax, frame_on=True)
    plt.setp(ax.get_xticklabels(), visible=False)
    plt.setp(ax.get_yticklabels(), visible=False)
    plt.setp(ax.get_xticklines(), visible=False)
    plt.setp(ax.get_yticklines(), visible=False)
    plt.savefig('images/primes_'+str(alpha)+'_'+str(beta)+'_'+str(gamma)+'.png',dpi=200, facecolor='k', edgecolor='k', bbox_inches='tight', pad_inches=0.1)
    plt.close()
 
 
def f(t, alpha, beta, gamma):
    return np.exp(alpha*1.0j*t) + np.exp(beta*1.0j*t) + np.exp(gamma*1.0j*t)
 
t = np.linspace(0, 2*np.pi, 3000000)
primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]#, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]


for i, alpha in enumerate(primes):
    for j,beta in enumerate(primes[i+1: len(primes) ]):
        for gamma in primes[i+j+2 : len(primes)]:
            Z = f(t,alpha,beta,gamma) / 3
            plt.plot(np.real(Z), np.imag(Z),'w-', lw=0.4) 
            saveit(alpha,beta,gamma)
