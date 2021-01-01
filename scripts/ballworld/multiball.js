// Copyright (c) 2020 Neil D. Lawrence

let entropyMultiball = document.getElementById("multiball-entropy");
entropyMultiball.value = 0.00

class Multiball extends HistogramGame {
    constructor(objects, params, simulation, boundaries, context, colors)
    {
	let histogram = {
	    nbins: 40,
	    min: -20,
	    max: 20
	};
	super(objects, params, simulation, boundaries, context, colors, histogram);
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
    demon() {
	super.demon();
	entropyMultiball.value = this.entropy.toFixed(4);
    }
	
    
}


let newballMultiballButton = document.getElementById("multiball-newball");
let pauseMultiballButton = document.getElementById("multiball-pause");
let histMultiballButton = document.getElementById("multiball-histogram");
let skipMultiballButton = document.getElementById("multiball-skip");


newballMultiballButton.addEventListener("click", function() {
    multiball.reset();
});
pauseMultiballButton.addEventListener("click", function() {
    multiball.togglePause();
});

histMultiballButton.addEventListener("click", function() {
    histogramSpeeds(multiball, "multiball-histogram-canvas");
});

skipMultiballButton.addEventListener("click", function() {
    multiball.toggleDraw();
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
