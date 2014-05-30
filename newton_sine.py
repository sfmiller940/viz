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
    gamma = math.pi * psi( psi( percent ) )
    alpha = complex( - math.cos( gamma ) , math.sin( gamma ) )
    beta = complex( math.cos( gamma ) ,  - math.sin( gamma ) )
    # put any complex function here to generate a fractal for it!
    def f(z):
        return ( (z - alpha) * (z - beta) * cmath.cos( halfpi * z ) )
    def df(z):
        return ( ( (z - beta) * cmath.cos( halfpi * z  ) ) + ( (z - alpha) * cmath.cos( halfpi * z ) ) - ( halfpi * (z - alpha) * (z - beta) * cmath.sin( halfpi * z ) ) )
    for y in range(imgy):
        zy = y * (yb - ya) / (imgy - 1) + ya
        for x in range(imgx):
            zx = x * (xb - xa) / (imgx - 1) + xa
            z = complex(zx, zy)
            for i in range(maxIt):
                #z = complex( round(z.real, 3), round(z.imag, 3)   )
                z =  z - f(z) / df(z) # Newton iteration
                cmap = cm.PRGn_r 
                if ( abs( z - round(z.real) ) < eps ) and ( int( round(z.real) ) & 0x1 ) : #Stop when close enough to odd integer.
                    cmap = cm.gist_ncar_r
                    break
                elif abs(z - alpha) < eps: # stop when close enough to any root
                    cmap = cm.jet
                    break
                elif abs(z - beta) < eps: # stop when close enough to any root
                    cmap = cm.jet_r
                    break
                elif abs(z) > 100:
                    break
            image.putpixel((x, y),  color_convert( cmap( 1.0 * i / maxIt  ) ) )
    image.save("newsine{:04}.png".format(frame), "PNG")
