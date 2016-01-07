import numpy as np
import matplotlib.pyplot as plt

frames = 720
steps = 10000
t = np.linspace(0, 2*np.pi, steps)
alpha = 11
beta = 29
gamma = 101
alpha0 = alpha
beta0 = beta
gamma0 = gamma
delta = 12.0 / frames

def f(t, alpha, beta, gamma):
    return np.exp(1j*t*alpha) + np.exp(1j*t*beta) + np.exp(1j*t*gamma)

for frame in range(frames + 1):
    Z = f(t, alpha, beta, gamma) 
    plt.plot(np.real(Z), np.imag(Z), 'w-', lw=0.2)
    #for index in range(len(Z) - 1 ):
        #percent = 1.0 * index / steps
        #theta = 0.5 - ( 0.5 * np.cos( 2 * np.pi * percent ) )
        #plt.plot([np.real(Z[index]),np.real(Z[index + 1])],[np.imag(Z[index]),np.imag(Z[index+1])],'-',alpha = 1 , lw=1, color = plt.cm.ocean( theta ) )
    
    f80 = plt.gcf()
    ax=f80.gca()
    ax.axis('off')
    ax.set_aspect('equal')
    plt.setp(ax, frame_on=True)
    plt.setp(ax.get_xticklabels(), visible=False)
    plt.setp(ax.get_yticklabels(), visible=False)
    plt.setp(ax.get_xticklines(), visible=False)
    plt.setp(ax.get_yticklines(), visible=False)
    plt.savefig("mysteries{:04}.png".format(frame),dpi=300, facecolor='k', edgecolor='k', bbox_inches='tight', pad_inches=0.1)
    plt.close()
    theta = 1 - np.cos( np.pi * ( (frame % (frames / 6) ) + 1 ) / (frames / 6 ) ) 
    if frame < frames / 6 :
        alpha = alpha0 + theta
    elif frame < frames / 3 :
        beta = beta0 + theta
    elif frame < frames / 2:
        gamma = gamma0 + theta
    elif frame < 2 * frames / 3:
        beta = beta0 + 2 - theta
    elif frame < 5 * frames / 6:
        alpha = alpha0 + 2 - theta
    else:
        gamma = gamma0 + 2 - theta

