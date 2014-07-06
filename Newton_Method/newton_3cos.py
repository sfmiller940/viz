#Newton Fractals
from PIL import Image
from pylab import *
import cmath

halfpi =  math.pi / 2 

imgx = 768 #576
imgy = 432 #324
image = Image.new("RGB", (imgx, imgy))

# drawing area
xa = -3.84
xb = 3.84
ya = -2.16
yb = 2.16

maxIt = 30 # max iterations allowed
eps = 1.0e-3 # max error allowed

frames = 1500 # number of frames in movie

def color_convert(RGBA):
    return (int( 255 * RGBA[0]), int( 255 * RGBA[1] ), int( 255 * RGBA[2]))

def psi(percent):
    return 0.5 - ( 0.5 * math.cos( percent * math.pi ) )

# draw the fractals
for frame in range(237, frames + 1 ):
    percent = 1.0 * frame / frames
    # parametrized paths for alpha and beta
    theta = math.pi * psi( percent )
    alpha = cmath.rect( math.sin( theta  * 5 ) , 2 * theta  )
    beta = cmath.rect(  math.sin( theta * 4 ) , - 3 * theta  )
    gamma = cmath.rect( math.sin( theta * 3 ) , 4 * theta  )
    delta = cmath.rect( 1.5 * math.sin( theta ) , 2 * theta - halfpi )
    # parametrized function of z and its derivative
    def f():
        return ( ( z - delta ) * cmath.cos( halfpi * alphaz ) * cmath.cos( halfpi * betaz ) * cmath.cos( halfpi * gammaz ) )
    def df():
        acos = cmath.cos( halfpi * alphaz )
        bcos = cmath.cos( halfpi * betaz )
        gcos = cmath.cos( halfpi * gammaz )
        return ( ( acos * bcos * gcos) - ( ( z - delta ) * acos * bcos * halfpi * gamma * cmath.sin( halfpi * gammaz) ) - ( ( z - delta ) * acos * gcos * halfpi * beta * cmath.sin( halfpi * betaz) ) - ( ( z - delta ) * gcos * bcos * halfpi * alpha * cmath.sin( halfpi * alphaz) ) )
    # loop through mesh
    for y in range(imgy):
        zy = y * (yb - ya) / (imgy - 1) + ya
        for x in range(imgx):
            zx = x * (xb - xa) / (imgx - 1) + xa
            z = complex(zx, zy) # mesh point
            cmap = cm.PRGn_r # default colormap
            for i in range(maxIt):
                alphaz = alpha * z
                betaz = beta * z
                gammaz = gamma * z
                z =  z - f() / df() # Newton iteration
                if abs( z - delta ) < eps: # if z is close to beta
                    cmap = cm.terrain
                    break
                elif ( abs( alphaz - round(alphaz.real) ) < eps ) and ( int( round(alphaz.real) ) & 0x1 ) : # if z is close to odd integer.
                    cmap = cm.gist_ncar_r
                    break
                elif ( abs( betaz - round(betaz.real) ) < eps ) and ( int( round(betaz.real) ) & 0x1 ) : # if z is close to alpha
                    cmap = cm.hsv
                    break
                elif ( abs( gammaz - round(gammaz.real) ) < eps ) and ( int( round(gammaz.real) ) & 0x1 ) : # if z is close to beta
                    cmap = cm.Paired_r
                    break
                elif abs(z) > 100: # if z is big
                    break
            image.putpixel((x, y),  color_convert( cmap( 1.0 * i / maxIt  ) ) ) # color z's pixel
    image.save("3cos{:04}.png".format(frame), "PNG") # save image
