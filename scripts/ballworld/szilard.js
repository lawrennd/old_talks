// Copyright (c) 2020 Neil D. Lawrence

class Szilard extends Game {
    constructor(objects, params, simulation, boundaries, context, colors) {
	super(objects, params, simulation, boundaries, context, colors);
	this.objects.membranes[this.objects.membranes.length] = new Box(this.context, this.context.canvas.width/2-5, 0, 5, this.context.canvas.height, this.colors.cold);
	this.objects.membranes[this.objects.membranes.length] = new Box(this.context, this.context.canvas.width/2, 0, 5, this.context.canvas.height, this.colors.hot);
	
    }
    birth(game) {
	var radius = 10;
	var i = 1;
	var temp = new Ball(this.context,
			    radius, this.context.canvas.height/2,
			    radius);
	temp.dy = 0.0;
	temp.dx = this.params.initialSpeed;
	this.objects.balls[this.objects.balls.length] = temp;    
    }
    demon() {
	for (var obj in this.objects.balls) {
	    var velocity = Math.sqrt(this.objects.balls[obj].dx*this.objects.balls[obj].dx + this.objects.balls[obj].dy*this.objects.balls[obj].dy);
	    if(this.objects.balls[obj].x < this.context.canvas.width/2-5-this.objects.balls[obj].radius)
	    {
		if(velocity>this.params.demonThreshold){
		    this.objects.balls[obj].color = this.colors.hot
		    this.objects.balls[obj].membraneImmune = true;
		} else {
		    this.objects.balls[obj].color = this.colors.cold
		    this.objects.balls[obj].membraneImmune = false;
		}
		
	    }
	    if(this.objects.balls[obj].x > this.context.canvas.width/2+5+this.objects.balls[obj].radius){
		if(velocity>this.params.demonThreshold){
		    this.objects.balls[obj].color = this.colors.hot
		    this.objects.balls[obj].membraneImmune = false;
		} else {
		    this.objects.balls[obj].color = this.colors.cold
		    this.objects.balls[obj].membraneImmune = true;
		}
	    }
	}
    }
    
    reset() {
	this.objects.balls = [];
	this.birth();
    }
}


var newballSzilardButton = document.getElementById("szilard-newball");
var pauseSzilardButton = document.getElementById("szilard-pause");

newballSzilardButton.addEventListener("click", function() {
    szilard.reset();
});
pauseSzilardButton.addEventListener("click", function() {
    szilard.togglePause();
});

// document.addEventListener("keydown", function() {
//     keyDownHandler(event, szilard);
// });
// document.addEventListener("keyup", function() {
//     keyUpHandler(event, szilard);
// });

var colors = {
    ground: 'rgba(56, 256, 56, 0.8)',
    pin: 'rgba(256, 56, 56, 0.8)',
    ball: 'rgba(200, 200, 200, 0.8)',
    membrane: 'rgba(56, 256, 56, 0.8)',
    hot: 'rgba(256, 56, 56, 0.8)',
    cold: 'rgba(56, 56, 256, 0.8)'
};

var simulation = {
    paused: true,
    gravity: false,
    drag: false,
    sound: false,
    clearCanv: true,
    dt: 1    
};

var boundaries = {
    wallBounce: true,
    floorBounce: true,
    floorWrap: false,
    floorWrapCenter: true,
    floorReset: false
};

var params = {
    inelasticityFactor: 1.0,
    demonThreshold: 3,
    initialSpeed: 5,
    energy: 0.0,
    gravityAccel: 0.06,
    arrowAccel: 0.4,
    stochasticity: 0.0,
    stochasticityScale: 0.2,
    dragFactor: 1.0
};

var objects = {
    balls: [],
    boxes: [],
    pits: [],
    posts: [],
    membranes: []
};

var context = {
    canvas: document.getElementById("szilard-canvas")
};

var szilard = new Szilard(objects, params, simulation, boundaries, context, colors);


szilard.reset();

draw(szilard);
