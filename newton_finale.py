#Newton Fractals
from PIL import Image
from pylab import *
import cmath

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

frames = 100 # number of frames in movie

def color_convert(RGBA):
    return (int( 255 * RGBA[0]), int( 255 * RGBA[1] ), int( 255 * RGBA[2]))

def psi(percent):
    return 0.5 - ( 0.5 * math.cos( percent * math.pi ) )

# draw the fractals
for frame in range(0, frames ):
    percent = 1.0 * frame / frames
    # parametrized paths for alpha and beta
    theta = math.pi * psi( percent )
    gamma = 2 * theta
    alpha = cmath.rect( math.sin( theta * math.pi * 4) , 2 * math.pi * theta  )
    beta = cmath.rect( 2 * math.sin( theta * math.pi * 3) , - 4 * math.pi * theta  )
    # parametrized function of z and its derivative
    def f(z):
        return ( (z - alpha) * (z - beta) * cmath.cos( halfpi * gamma * z ) )
    def df(z):
        return ( ( (z - beta) * cmath.cos( halfpi * gamma * z  ) ) + ( (z - alpha) * cmath.cos( halfpi * gamma * z ) ) - ( halfpi * gamma * (z - alpha) * (z - beta) * cmath.sin( halfpi * gamma * z ) ) )
    # loop through mesh
    for y in range(imgy):
        zy = y * (yb - ya) / (imgy - 1) + ya
        for x in range(imgx):
            zx = x * (xb - xa) / (imgx - 1) + xa
            z = complex(zx, zy) # mesh point
            cmap = cm.PRGn_r # default colormap
            for i in range(maxIt):
                z =  z - f(z) / df(z) # Newton iteration
                gammaz = gamma * z
                if ( abs( gammaz - round(gammaz.real) ) < eps ) and ( int( round(gammaz.real) ) & 0x1 ) : # if z is close to odd integer.
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
    image.save("finale{:04}.png".format(frame), "PNG") # save image
