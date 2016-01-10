import matplotlib.pyplot as plt
import numpy as np
 
def f(t):
    return np.exp(17j*t) + np.exp(57j*t) + np.exp(67j*t) + np.exp(91j*t)
 
t = np.linspace(0, 2*np.pi, 1000000)
Z = f(t)

plt.plot(np.real(Z), np.imag(Z))
 
# These two lines make the aspect ratio square
fig = plt.gcf()
fig.gca().set_aspect('equal')
 
plt.show()
