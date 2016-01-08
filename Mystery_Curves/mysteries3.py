import numpy as np
import matplotlib.pyplot as plt

frames = 120
steps = 10000
t = np.linspace(0, 2*np.pi, steps)

alpha = 1
beta = 0
gamma = 0
delta = 0

def f(t, alpha, beta, gamma):
    return (alpha * np.exp(11j*t)) + (beta * np.exp(41j*t)) + (gamma * np.exp(101j*t)) + (delta * np.exp(23j*t) )

for frame in range(frames+1):
    percent = 1.0 * frame / frames
    if frame < frames / 6:
        theta = ( 1 - np.cos( np.pi * percent * 6 ) ) / 4
        alpha = 1 - theta
        beta = theta
    elif frame < frames / 3:
        theta = ( 1 - np.cos( np.pi * ( percent - (1.0/6) ) * 6 ) ) / 6
        gamma = theta
        alpha = 0.5 - (theta / 2)
        beta = 0.5 - (theta / 2)
    elif frame < frames / 2:
        theta = ( 1 - np.cos( np.pi * ( percent - (1.0/3) ) * 6 ) ) / 8
        alpha = (1.0/3) - (theta /3 )
        beta = (1.0 / 3) - (theta / 3)
        gamma = (1.0 /3 ) - (theta / 3)
        delta = theta
    elif frame < 2 * frames / 3:
        theta = ( 1 - np.cos( np.pi * ( percent - (0.5) ) * 6 ) ) / 8
        alpha = 0.25 + (theta /3 )
        beta = 0.25 - theta
        gamma = 0.25 + (theta / 3)
        delta = 0.25 + (theta / 3)        
    elif frame < 5 * frames / 6:
        theta = ( 1 - np.cos( np.pi * ( percent - (2.0/3) ) * 6 ) ) / 6
        gamma = (1.0/3) + ( theta / 2 )
        alpha = (1.0/3) - theta
        delta = (1.0/3) + (theta / 2)
    else:
        theta = ( 1 - np.cos( np.pi * ( percent - (5.0/6) ) * 6 ) ) / 4 
        gamma = 0.5 + theta
        delta = 0.5 - theta

        
    Z = f(t, alpha, beta, gamma) 
    plt.plot(np.real(Z), np.imag(Z), 'w-', lw=0.4)
    #for index in range(len(Z) - 1 ):
        #subcent = 1.0 * index / steps
        #theta = 0.5 - ( 0.5 * np.cos( 2 * np.pi * percent ) )
        #plt.plot([np.real(Z[index]),np.real(Z[index + 1])],[np.imag(Z[index]),np.imag(Z[index+1])],'-',alpha = 1 , lw=0.5, color = plt.cm.hsv( (subcent + (6 * percent))%1 ) )
    
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
    plt.savefig("mysteries{:04}.png".format(frame),dpi=200, facecolor='k', edgecolor='k', bbox_inches='tight', pad_inches=0.1)
    plt.close()
