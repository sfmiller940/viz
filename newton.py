#Newton Fractals, hacked from: http://code.activestate.com/recipes/577166-newton-fractals/
from PIL import Image
from pylab import *
imgx = 768
imgy = 432
image = Image.new("RGB", (imgx, imgy))

# drawing area
xa = -2.5
xb = 5.0
ya = -2.0
yb = 2.0

maxIt = 20 # max iterations allowed
h = 0.5e-6 # step size for numerical derivative
eps = 1e-4 # max error allowed

frames = 500 # number of frames in movie

def color_convert(RGBA):
    return (int( 255 * RGBA[0]), int( 255 * RGBA[1] ), int( 255 * RGBA[2]))

# draw the fractals
for frame in range(0, frames + 1 ):
    percent = 1.0 * frame / frames
    #alpha = 0.5 - ( 0.5 * math.cos( percent * math.pi ) )
    # put any complex function here to generate a fractal for it!
    def f(z):
        return ( percent * z * z * z ) + ( z * z ) + 1
    for y in range(imgy):
        zy = y * (yb - ya) / (imgy - 1) + ya
        for x in range(imgx):
            zx = x * (xb - xa) / (imgx - 1) + xa
            z = complex(zx, zy)
            for i in range(maxIt):
                # complex numerical derivative
                dz = (f(z + complex(h, h)) - f(z)) / complex(h, h)
                z0 = z - f(z) / dz # Newton iteration
                if abs(z0 - z) < eps: # stop when close enough to any root
                    break
                z = z0
            #image.putpixel((x, y), (i % 4 * 64, i % 16 * 16, i % 32 * 8))
            image.putpixel((x, y),  color_convert( cm.ocean_r( 1.0 * i / maxIt  ) ) )
    image.save("test{:04}.png".format(frame), "PNG")
