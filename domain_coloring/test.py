import Image
import colorsys
import math as math
import numpy as np
import cmath as cmath

size = 400
width = 11.0
frames = 100

for frame in range(frames):
	img = Image.new( 'RGB', ( 3 * size / 2 ,size), "black") # create a new black image
	pixels = img.load() # create the pixel map
	gamma = 0.5 - ( 0.5 * math.cos( frame * 2 * math.pi / frames ) )

	for i in range(img.size[0]):    # for every pixel:
	    for j in range(img.size[1]):
	        x = 1.5 * ( ( width * i / img.size[0] ) - ( width / 2 ) )
	        y = ( width * j / img.size[1] ) - ( width / 2 )
	        z = y + ( 1.0j * x )
	        if frame < frames / 2:
	        	z = z + ( gamma * ( cmath.tan( z ) + cmath.exp( z * gamma ) ) ) 
	        else:
	        	z = z + ( gamma * ( cmath.tan( gamma * z ) + cmath.exp( z ) ) ) 
	        phase = cmath.phase(z)
	        if phase < 0 : phase = ( 2 * math.pi ) + phase
	        H = phase / (2 * math.pi)
	        S = 1
	        V = 0.75 - ( 0.25 * math.cos( np.abs(z) * 3 * math.pi ) ) 
	        color = list( colorsys.hsv_to_rgb( H , S , V ) )
	        for k in range(3): color[k] = int( 255 * color[k] )
	        pixels[i,j] = tuple(color) # set the colour accordingly

	#img.show()
	img.save("expintanout{:04}.png".format(frame))
