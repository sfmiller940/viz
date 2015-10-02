import Image
import colorsys
import math as math
import numpy as np
import cmath as cmath

size = 800
width = 13.0
frames = 20

for frame in range(frames):
	img = Image.new( 'RGB', (size,size), "black") # create a new black image
	pixels = img.load() # create the pixel map

	for i in range(img.size[0]):    # for every pixel:
	    for j in range(img.size[1]):
	        x = ( width * i / size ) - ( width / 2 )
	        y = ( width * j / size ) - ( width / 2 )
	        z = x + ( 1.0j * y )
	        z = cmath.tan(z) + (frame * cmath.exp(z) / frames )
	        phase = cmath.phase(z)
	        if phase < 0 : phase = ( 2 * math.pi ) + phase
	        H = phase / (2 * math.pi)
	        S = 1
	        V = 0.75 - ( 0.25 * math.cos( np.abs(z) * 3 * math.pi ) ) 
	        color = list( colorsys.hsv_to_rgb( H , S , V ) )
	        for k in range(3): color[k] = int( 255 * color[k] )
	        pixels[i,j] = tuple(color) # set the colour accordingly

	img.show()
