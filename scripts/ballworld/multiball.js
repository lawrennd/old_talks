// Copyright (c) 2020 Neil D. Lawrence


class Multiball extends Game {
    constructor(objects, params, simulation, boundaries, context, colors)
    {
	super(objects, params, simulation, boundaries, context, colors);
	const nbins = 40;
	const minSpeed = -20;
	const maxSpeed = 20;
	const gap = (maxSpeed-minSpeed)/nbins;
	this.histogram = {
	    nbins: nbins,
	    minSpeed: minSpeed,
	    maxSpeed: maxSpeed,
	    gap: gap,
	    y: new Array(nbins).fill(0),
	    x: new Array(nbins),
	    width: new Array(nbins).fill(gap),
	    sum: 0,
	}
	for(let i=0; i<nbins; i++) {
	    this.histogram.x[i] = i*gap+minSpeed;
	}
	
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
    
	for (let i = 0; i < this.objects.balls.length; i++) {
	    let dx = this.objects.balls[i].dx-this.histogram.minSpeed;
	    let dy = this.objects.balls[i].dy-this.histogram.minSpeed;
	    for (let j=0; j<this.histogram.nbins; j++) {
		if(dx > j*this.histogram.gap && dx < (j+1)*this.histogram.gap) {
		    this.histogram.y[j]++;
		    this.histogram.sum++;

		}
		if(dy > j*this.histogram.gap && dy < (j+1)*this.histogram.gap) {
		    this.histogram.y[j]++;
		    this.histogram.sum++;

		}
	    }
	}
	if (this.simulation.time % 1000 == 0) {
	    this.simulation.draw=true;
	    
	}
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


let histButton = document.getElementById("multiball-histogram");

histButton.addEventListener("click", function() {
    histogramSpeeds(multiball);
});

let skipButton = document.getElementById("multiball-skip");

skipButton.addEventListener("click", function() {
    multiball.toggleDraw();
});

function histogramSpeeds(game) {
	    const normCounts = game.histogram.y.map(x => x/game.histogram.sum);
	    let trace = {
		type: 'bar', 
		x: game.histogram.x,
		y: normCounts,
		width: game.histogram.width,
		marker: {
		    color: 'grey'
		}
	    }
	    let data = [trace];
	    let layout = {
		paper_bgcolor: "rgba(0,0,0,0)",		
		plot_bgcolor: "rgba(0,0,0,0)",
		xaxis: {range: [game.histogram.minSpeed, game.histogram.maxSpeed]},
		yaxis: {range: [0, 0.13]}
	    };
	    Plotly.newPlot("multiball-histogram-canvas", data, layout);
}

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
