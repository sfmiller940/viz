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

	var maxIt = 20;
	var eps = 0.005;
	var zalpha, zbeta,zgamma;
		
	// Zero points. Clean up into an object.
	var alpha = math.complex(Math.random(), Math.random());
	var beta = math.complex(Math.random(), Math.random());
	var gamma = math.complex(Math.random(), Math.random());
	var alphaD = 2 * Math.PI * Math.random();
	var betaD = 2 * Math.PI * Math.random();
	var gammaD = 2 * Math.PI * Math.random();
	var delta = 1 / width;
	// Clean up to keep within boundaries.
	var moveGreeks = function(){
		alpha = math.add( alpha, math.multiply( delta, math.complex( Math.cos( alphaD ), Math.sin( alphaD ) ) ) );	
		beta = math.add( beta, math.multiply( delta, math.complex( Math.cos( betaD ), Math.sin( betaD ) ) ) );	
		gamma = math.add( gamma, math.multiply( delta, math.complex( Math.cos( gammaD ), Math.sin( gammaD ) ) ) );	
	};
	
	var F = function(){
		return math.multiply(zalpha,math.multiply(zbeta, zgamma));
	};
	
	var dF = function(){
		return math.add(math.multiply(zalpha,zbeta),math.add(math.multiply(zalpha,zgamma),math.multiply(zbeta,zgamma)));
	};
	
	// Main loop	
	var drawNewt = function(){
		ctx.clearRect(0,0,width,height);
		moveGreeks();
		for(var i = 0;i < width;i++){
			var zx = i / width;
			for(var j=0;j<height;j++){
				var zy = j / width;
				var z = math.complex(zx, zy);
				var fillColor = "rgba(0,0,0,1)";
				for(var loop=0; loop<maxIt; loop++){
					zalpha = math.subtract(z,alpha);
					zbeta = math.subtract(z,beta);
					zgamma = math.subtract(z,gamma);
					z =  math.subtract(z , math.divide( F() , dF() ) );
					if (math.abs(math.subtract(z, alpha)) < eps){
						fillColor = "rgba(255,255,0,"+ (loop/maxIt) +")";
						break;
					}
					else if (math.abs(math.subtract(z, beta)) < eps){
						fillColor = "rgba(0,255,255,"+ (loop/maxIt) +")";
						break;
					}
					else if (math.abs(math.subtract(z, gamma)) < eps){ 
						fillColor = "rgba(255,0,255,"+ (loop/maxIt) +")";
						break;
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
