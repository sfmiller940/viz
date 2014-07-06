#Newton Fractals
from PIL import Image
from pylab import *
import cmath

halfpi =  math.pi / 2 

imgx = 700 #576
imgy = 500 #324
image = Image.new("RGB", (imgx, imgy))

# drawing area
xa = -3.5
xb = 3.5
ya = -2.5
yb = 2.5

maxIt = 30 # max iterations allowed
eps = 1.0e-3 # max error allowed

frames = 1800 # number of frames in movie

def color_convert(RGBA):
    return (int( 255 * RGBA[0]), int( 255 * RGBA[1] ), int( 255 * RGBA[2]))

def psi(percent):
    return 0.5 - ( 0.5 * math.cos( percent * math.pi ) )

# draw the fractals
for frame in range(0, frames + 1 ):
    percent = 1.0 * frame / frames
    # parametrized paths for alpha and beta
    theta = math.pi * psi( percent )
    gamma = cmath.rect( 2 * math.sin( 2 * theta ) , 2 * theta * math.sin( 2 * theta )  )
    alpha = cmath.rect( 2 * math.sin( theta  * 5 ) , 2 * theta  )
    beta = cmath.rect( 2 * math.sin( theta * 4 ) , - 3 * theta  )
    delta = cmath.rect( 2 * math.sin( theta * 3 ) , 4 * theta  )
    # parametrized function of z and its derivative
    def f(z):
        return ( (z - alpha) * (z - beta) * (z - delta) * cmath.cos( halfpi * gamma * z ) )
    def df(z):
        za = z - alpha
        zb = z - beta
        zd = z - delta
        cosz = cmath.cos( halfpi * gamma * z )
        return ( ( za * zb * cosz ) + ( za * zd * cosz ) + ( zb * zd * cosz ) - ( halfpi * gamma * za * zb * zd * cmath.sin( halfpi * gamma * z ) ) )
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
                    cmap = cm.terrain
                    break
                elif abs(z - alpha) < eps: # if z is close to alpha
                    cmap = cm.hsv
                    break
                elif abs(z - beta) < eps: # if z is close to beta
                    cmap = cm.gist_ncar_r
                    break
                elif abs(z - delta) < eps: # if z is close to beta
                    cmap = cm.Paired_r
                    break
                elif abs(z) > 100: # if z is big
                    break
            image.putpixel((x, y),  color_convert( cmap( 1.0 * i / maxIt  ) ) ) # color z's pixel
    image.save("trip{:04}.png".format(frame), "PNG") # save image
