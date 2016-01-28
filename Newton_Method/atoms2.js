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

	var maxIt = 16;
	var eps = 0.005;
	var zalpha, zbeta,zgamma;
		
	// Zero points. Clean up into an object.
	function zeroPt(fillHue){

		this.loc = math.complex(Math.random(), height * Math.random() / width );
		this.dir = 2 * Math.PI * Math.random();
		this.delta = 1 / Math.max( width, height );
		this.fillHue = fillHue;
		
		this.update = function(){
			
				// Move point;
				var newpoint = math.add(this.loc, math.multiply( this.delta, math.complex( Math.cos(this.dir), Math.sin(this.dir) ) ) );
				while( math.re(newpoint) < 0 || 1 < math.re(newpoint) || math.im(newpoint) < 0 || height / width < math.im(newpoint) ){
					this.dir = 2 * Math.PI * Math.random();
					newpoint = math.add(this.loc, math.multiply( this.delta, math.complex( Math.cos(this.dir), Math.sin(this.dir) ) ) );
				}
				this.loc = newpoint;
				
				this.fillHue = (this.fillHue + 1) % 360;
				
			};
	}
	
	var zeroPts = [ new zeroPt(0), new zeroPt(120), new zeroPt(240) ];
		
	var F = function(){
		return math.multiply(zalpha,math.multiply(zbeta, zgamma));
	};
	
	var dF = function(){
		return math.add(math.multiply(zalpha,zbeta),math.add(math.multiply(zalpha,zgamma),math.multiply(zbeta,zgamma)));
	};
	
	// Main loop	
	var drawNewt = function(){
		ctx.clearRect(0,0,width,height);
		for(var i=0; i< zeroPts.length;i++){ 	zeroPts[i].update(); }
		
		for(var i = 0;i < width;i++){
			var zx = i / width;
			for(var j=0;j<height;j++){
				var zy = j / width;
				var z = math.complex(zx, zy);
				var fillColor = 'rgba(0,0,0,1.0)';
				var RGB = [0,0,0];
				iterLoop: for(var loop=0; loop<maxIt; loop++){
					zalpha = math.subtract(z,zeroPts[0].loc);
					zbeta = math.subtract(z,zeroPts[1].loc);
					zgamma = math.subtract(z,zeroPts[2].loc);
					z =  math.subtract(z , math.divide( F() , dF() ) );
					for( var k = 0; k < zeroPts.length; k++){
						if (math.abs(math.subtract(z, zeroPts[k].loc )) < eps){
							
							if( (loop / maxIt) < 0.5 ) { RGB = hsvToRgb(  zeroPts[k].fillHue, 100 * Math.sin( Math.PI * loop / maxIt ) , 100); }
							else{ RGB = hsvToRgb(  zeroPts[k].fillHue, 100 , 100 * Math.sin( Math.PI * loop / maxIt ) ); }
							
							fillColor = "rgba("+ RGB[0] +","+ RGB[1] +","+ RGB[2] +","+ (loop/maxIt) +")";
							break iterLoop;
						}
					}
				}
			ctx.fillStyle = fillColor;
			ctx.fillRect( i, j, 1, 1 );
			}
		}
		window.requestAnimationFrame(drawNewt);
	};
	
	window.requestAnimationFrame(drawNewt);
	
};
