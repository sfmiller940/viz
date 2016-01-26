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
    plt.savefig('images/prime_print_'+str(alpha)+'_'+str(beta)+'_'+str(gamma)+'.png',dpi=300, facecolor='k', edgecolor='k', bbox_inches='tight', pad_inches=0.1)
    plt.close()

alpha = 3
beta = 7
gamma = 43
steps = 10000

def f(t):
    return np.exp(alpha*1.0j*t) + np.exp(beta*1.0j*t) + np.exp(gamma*1.0j*t)
 
t = np.linspace(0, 2*np.pi, steps)
primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]#, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]


Z = f(t) / 3
#plt.plot(np.real(Z), np.imag(Z),'w-', lw=0.4) 
for index in range(len(Z) - 1 ):
    percent = 1.0 * index / steps
    plt.plot([np.real(Z[index]),np.real(Z[index + 1])],[np.imag(Z[index]),np.imag(Z[index+1])],'-',alpha = 1 , lw=0.5, color = plt.cm.hsv( percent ) )
saveit(alpha,beta,gamma)
