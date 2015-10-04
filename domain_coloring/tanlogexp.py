import Image
import colorsys
import math as math
import numpy as np
import cmath as cmath

size = 400
width = 7.0
frames = 160

for frame in range(frames):
	img = Image.new( 'RGB', ( 3 * size / 2 ,size), "black") # create a new black image
	pixels = img.load() # create the pixel map
	gamma = 0.5 - ( 0.5 * math.cos( frame * 4 * math.pi / frames ) )

	for i in range(img.size[0]):    # for every pixel:
	    for j in range(img.size[1]):
	        x = 1.5 * ( ( width * i / img.size[0] ) - ( width / 2 ) )
	        y = ( width * j / img.size[1] ) - ( width / 2 )
	        z = y + ( 1.0j * x )
	        if frame < frames / 4 :
	        	z = ( gamma * cmath.tan( z ) ) + ( (1 - gamma) * z ) 
	        elif frame < frames / 2 :
	        	if z == 0 : continue
	        	z = ( gamma * cmath.tan( z ) ) + ( (1 - gamma) * cmath.log(z) )  
	        elif frame < 3 * frames / 4:
	        	if z == 0 : continue
	        	z = ( gamma * cmath.exp( z ) ) + ( (1 - gamma) * cmath.log(z) ) 
	        else:
	        	z = ( gamma * cmath.exp(z) ) + ( (1 - gamma) * z ) 
	        H = 0.5  + ( cmath.phase(z) / ( 2 * math.pi) )
	        S = math.pow(np.abs(math.sin(2 * math.pi * np.abs(z) ) ), 0.5)
	        V = math.pow(np.abs( math.sin( z.real * 2 * math.pi ) * math.sin( z.imag * 2 * math.pi )), 0.25)
	        V = max( V, 1 - S )
	        color = list( colorsys.hsv_to_rgb( H , S , V ) )
	        for k in range(3): color[k] = int( 255 * color[k] )
	        pixels[i,j] = tuple(color) # set the colour accordingly

	#img.show()
	img.save("tanlogexp{:04}.png".format(frame))
