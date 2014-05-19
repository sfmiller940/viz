#Newton Fractals
from PIL import Image
from pylab import *
imgx = 768
imgy = 432
image = Image.new("RGB", (imgx, imgy))

# drawing area
xa = -2.5
xb = 2.5
ya = -1.5
yb = 1.5

maxIt = 30 # max iterations allowed
eps = 0.5e-4 # max error allowed

frames = 600 # number of frames in movie

def color_convert(RGBA):
    return (int( 255 * RGBA[0]), int( 255 * RGBA[1] ), int( 255 * RGBA[2]))

# draw the fractals
for frame in range(0, 301 ):
    percent = 1.0 * frame / frames
    theta = 0.5 - ( 0.5 * math.cos( percent * math.pi ) )
    gamma = 2.0 * theta * math.pi
    alpha = complex( 1 - math.cos( gamma ) , math.sin( gamma ) )
    beta = complex( -1 + math.cos( gamma ) , math.sin( gamma ) )
    # put any complex function here to generate a fractal for it!
    def f(z):
        return z * (z - alpha) * (z - beta)
    def df(z):
        return ( (z - alpha) * (z - beta) ) +  ( z  * (z - beta) ) + ( z * (z - alpha) )
    for y in range(imgy):
        zy = y * (yb - ya) / (imgy - 1) + ya
        for x in range(imgx):
            zx = x * (xb - xa) / (imgx - 1) + xa
            z = complex(zx, zy)
            for i in range(maxIt):
                z = z - f(z) / df(z) # Newton iteration
                if abs(z) < eps: # stop when close enough to any root
                    cmap = cm.gist_rainbow_r
                    break
                elif abs(z - alpha) < eps: # stop when close enough to any root
                    cmap = cm.gist_ncar_r
                    break
                elif abs(z - beta) < eps: # stop when close enough to any root
                    cmap = cm.Paired_r
                    break
            image.putpixel((x, y),  color_convert( cmap( 1.0 * i / maxIt  ) ) )

    fname='three'
    if frame < 10 : fname = fname + "000"
    elif frame < 100 : fname = fname + "00"
    elif frame < 1000 : fname = fname + "0"
    image.save(fname + str(frame) + ".png", "PNG")
