(function () {
   'use strict';
  
  	var frameCount = 0;
	window.onload = function(){
		// Canvas setup
		var canvas = document.getElementById('myCanvas');
		var ctx=canvas.getContext("2d");
		var width, height;
		var canvasInit = function(){
			width = window.innerWidth;
			height = window.innerHeight;	
			canvas.width = width;
			canvas.height = height ;
		};
		canvasInit();
		window.onresize = canvasInit;
				
		// Zero points. 
		function zeroPt(){
	
			this.loc = math.complex(width * Math.random(), height * Math.random() );
			this.dir = 2 * Math.PI * Math.random();
			this.delta = 1;
			
			this.update = function(){
				
					// Move point;
					var newpoint = math.add(this.loc, math.multiply( this.delta, math.complex( Math.cos(this.dir), Math.sin(this.dir) ) ) );
					while( math.re(newpoint) < 0 || width < math.re(newpoint) || math.im(newpoint) < 0 || height < math.im(newpoint) ){
						this.dir = 2 * Math.PI * Math.random();
						newpoint = math.add(this.loc, math.multiply( this.delta, math.complex( Math.cos(this.dir), Math.sin(this.dir) ) ) );
					}
					this.loc = newpoint;
										
				};
		}
		var zeroPts = [new zeroPt(),new zeroPt(),new zeroPt(),new zeroPt(),new zeroPt(),new zeroPt()];
			
		// Main loop	
		var colorDomain = function(){
			
			ctx.clearRect(0,0,width,height);
			
			for(var i=0; i< zeroPts.length;i++){ 	zeroPts[i].update(); }
			
			for(var i = 0;i < width;i++){
				for(var j=0;j<height;j++){
					var z = math.complex(i,j);
					z = math.divide( math.multiply( math.subtract(z,zeroPts[0].loc) , math.multiply( math.subtract(z,zeroPts[1].loc), math.subtract(z,zeroPts[2].loc)) ), math.multiply( math.subtract(z,zeroPts[3].loc), math.multiply( math.subtract(z,zeroPts[4].loc), math.subtract(z,zeroPts[5].loc)) ) );
					var H = math.arg(z) / ( 2 * Math.PI);
					var S = Math.pow(Math.abs(Math.sin(2 * Math.PI * math.abs(z) ) ), 0.5);
					var V = Math.pow(Math.abs( Math.sin( math.re(z) * 2 * Math.PI ) * Math.sin( math.im(z) * 2 * Math.PI )), 0.25);
					V = Math.max( V, 1 - S );
					var RGB = hsvToRgb(((360 * H) + (4*frameCount)) % 360, 100 * S, 100 * V);
					var fillColor = "rgba("+ RGB[0] +","+ RGB[1] +","+ RGB[2] +",1)";
					ctx.fillStyle = fillColor;
					ctx.fillRect( i, j, 1, 1 );
				}
			}
			frameCount++;
			window.requestAnimationFrame(colorDomain);
		};
		
		window.requestAnimationFrame(colorDomain);
		
	};
	
	function hsvToRgb(h, s, v) {
		var r, g, b;
		var i;
		var f, p, q, t;
		
		// Make sure our arguments stay in-range
		h = Math.max(0, Math.min(360, h));
		s = Math.max(0, Math.min(100, s));
		v = Math.max(0, Math.min(100, v));
		
		// We accept saturation and value arguments from 0 to 100 because that's
		// how Photoshop represents those values. Internally, however, the
		// saturation and value are calculated from a range of 0 to 1. We make
		// That conversion here.
		s /= 100;
		v /= 100;
		
		if(s == 0) {
			// Achromatic (grey)
			r = g = b = v;
			return [Math.round(r * 255), Math.round(g * 255), Math.round(b * 255)];
		}
		
		h /= 60; // sector 0 to 5
		i = Math.floor(h);
		f = h - i; // factorial part of h
		p = v * (1 - s);
		q = v * (1 - s * f);
		t = v * (1 - s * (1 - f));
	
		switch(i) {
			case 0:
				r = v;
				g = t;
				b = p;
				break;
				
			case 1:
				r = q;
				g = v;
				b = p;
				break;
				
			case 2:
				r = p;
				g = v;
				b = t;
				break;
				
			case 3:
				r = p;
				g = q;
				b = v;
				break;
				
			case 4:
				r = t;
				g = p;
				b = v;
				break;
				
			default: // case 5:
				r = v;
				g = p;
				b = q;
		}
		return [Math.round(r * 255), Math.round(g * 255), Math.round(b * 255)];
	}
}());
