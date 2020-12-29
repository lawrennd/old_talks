// Copyright (c) 2020 Neil D. Lawrence


class Multiball extends Game {
    constructor(objects, params, simulation, boundaries, context, colors)
    {
	super(objects, params, simulation, boundaries, context, colors);
    }
    birth() {
	var radius = 10;
	var balls = 39;
	for (var i=3*radius; i<this.context.canvas.width; i+=2*radius + 1)
	{
	    var temp = new Ball(this.context, i, radius, radius);
	    temp.dx = Math.random()*1e-1;
	    temp.dy = this.params.initialSpeed;
	    temp.color = this.colors.ball;
	    this.objects.balls[this.objects.balls.length] = temp;
	}
    }
    reset() {
	this.objects.balls = [];
	this.birth();
    }

}


var newballButton = document.getElementById("multiball-newball");
var pauseButton = document.getElementById("multiball-pause");

newballButton.addEventListener("click", function() {
    multiball.reset();
});
pauseButton.addEventListener("click", function() {
    multiball.togglePause();
});

var colors = {
    ground: 'rgba(56, 256, 56, 0.8)',
    pin: 'rgba(256, 56, 56, 0.8)',
    ball: 'rgba(200, 200, 200, 0.8)'
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
    initialSpeed: 5,
    energy: 0.0,
    gravityAccel: 0.06,
    arrowAccel: 0.4,
    stochasticity: 0.0,
    stochasticityScale: 0.2,
    dragFactor: 0.0
};

var objects = {
    balls: [],
    boxes: [],
    pits: [],
    posts: [],
    membranes: []
};

var context = {
    canvas: document.getElementById("multiball-canvas")
};

var multiball = new Multiball(objects, params, simulation, boundaries, context, colors);

multiball.reset();
draw(multiball);
