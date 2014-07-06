#Newton Fractals
from PIL import Image
from pylab import *
import cmath
import mpmath

halfpi =  math.pi / 2 

imgx = 900 #576
imgy = 405 #324
image = Image.new("RGB", (imgx, imgy))

# drawing area
xa = -3.0
xb = 3.0
ya = -1.35
yb = 1.35

maxIt = 40 # max iterations allowed
eps = 1.0e-3 # max error allowed

frames = 600 # number of frames in movie

def color_convert(RGBA):
    return (int( 255 * RGBA[0]), int( 255 * RGBA[1] ), int( 255 * RGBA[2]))

def psi(percent):
    return 0.5 - ( 0.5 * math.cos( percent * math.pi ) )

# draw the fractals
for frame in range(0, ( frames / 2 )  + 1 ):
    percent = 1.0 * frame / frames
    # parametrized paths for alpha and beta
    gamma = math.pi * psi( percent )
    alpha = complex( - math.cos( gamma ) , math.sin( gamma ) )
    beta = complex( math.cos( gamma ) ,  - math.sin( gamma ) )
    # parametrized function of z and its derivative
    def f(z):
        return ( (z - alpha) * (z - beta) * cmath.cos( halfpi * z ) )
    def df(z):
        return ( ( (z - beta) * cmath.cos( halfpi * z  ) ) + ( (z - alpha) * cmath.cos( halfpi * z ) ) - ( halfpi * (z - alpha) * (z - beta) * cmath.sin( halfpi * z ) ) )
    # loop through mesh
    for y in range(imgy):
        zy = y * (yb - ya) / (imgy - 1) + ya
        for x in range(imgx):
            zx = x * (xb - xa) / (imgx - 1) + xa
            z = complex(zx, zy) # mesh point
            cmap = cm.PRGn_r # default colormap
            for i in range(maxIt):
                z =  z - f(z) / df(z) # Newton iteration
                if ( abs( z - round(z.real) ) < eps ) and ( int( round(z.real) ) & 0x1 ) : # if z is close to odd integer.
                    cmap = cm.gist_ncar_r
                    break
                elif abs(z - alpha) < eps: # if z is close to alpha
                    cmap = cm.jet
                    break
                elif abs(z - beta) < eps: # if z is close to beta
                    cmap = cm.jet_r
                    break
                elif abs(z) > 100: # if z is big
                    break
            image.putpixel((x, y),  color_convert( cmap( 1.0 * i / maxIt  ) ) ) # color z's pixel
    image.save("newsine{:04}.png".format(frame), "PNG") # save image
