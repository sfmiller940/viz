from PIL import Image
import colorsys
import math as math
import numpy as np
import cmath as cmath

size = 10000
width = 5

img = Image.new( 'RGB', ( int( 6 * size / 5) , size), 'black') # create a new black image
pixels = img.load() # create the pixel map

for frame in range(20):
    for i in range(img.size[0]):    # for every pixel:
        for j in range(img.size[1]):
    	        x = 1.2 * ( ( width * i / img.size[0] ) - ( width / 2 ) )
    	        y = ( width * j / img.size[1] ) - ( width / 2 )
    	        z = y + ( 1.0j * x )
    	        z = (2 - (z*z*z) ) / ( 2 + (z * z * z) ) 
    	        H = ((frame/20) + ( cmath.phase(z) / ( 2 * math.pi) ) ) % 1
    	        S = math.pow(np.abs(math.sin(2 * math.pi * np.abs(z) ) ), 0.5)
    	        V = math.pow(np.abs( math.sin( z.real * 2 * math.pi ) * math.sin( z.imag * 2 * math.pi )), 0.25)
    	        V = max( V, 1 - S )
    	        color = list( colorsys.hsv_to_rgb( H , S , V ) )
    	        for k in range(3): color[k] = int( 255 * color[k] )
    	        pixels[i,j] = tuple(color) # set the colour accordingly
    
    #img.show()
    img.save("domain_test{:04}.png".format(frame))
