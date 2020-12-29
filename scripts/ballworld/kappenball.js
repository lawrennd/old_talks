// Copyright (c) 2020 Neil D. Lawrence

class Kappenball extends Game {
    constructor(objects, params, simulation, boundaries, context, colors) {
	super(objects, params, simulation, boundaries, context, colors);

	
	this.holeWidth = 100;
	this.objects.pits[this.objects.pits.length] = new Box(this.context, 0, this.context.canvas.height-40, 90, 30, this.colors.pin);
	this.objects.boxes[this.objects.boxes.length] = new Box(this.context, 0, this.context.canvas.height-10, 90, 10, this.colors.ground);
	this.objects.posts[this.objects.posts.length] = new Post(this.context, 95, this.context.canvas.height-35, 5, this.colors.ground);
	this.objects.boxes[this.objects.boxes.length] = new Box(this.context, 90, this.context.canvas.height-30, 10, 20, this.colors.ground);
	this.objects.posts[this.objects.posts.length] = new Post(this.context, 95, this.context.canvas.height-5, 5, this.colors.ground);
	this.objects.posts[this.objects.posts.length] = new Post(this.context, 305, this.context.canvas.height-35, 5, this.colors.ground);
	this.objects.boxes[this.objects.boxes.length] = new Box(this.context, 300, this.context.canvas.height-30, 10, 20, this.colors.ground);
	this.objects.posts[this.objects.posts.length] = new Post(this.context, 305, this.context.canvas.height-5, 5, this.colors.ground);
	this.objects.boxes[this.objects.boxes.length] = new Box(this.context, 310, this.context.canvas.height-10, 280, 10, this.colors.ground);
	this.objects.pits[this.objects.pits.length] = new Box(this.context, 310, this.context.canvas.height-40, 280, 30, this.colors.pin);
	this.objects.posts[this.objects.posts.length] = new Post(this.context, 595, this.context.canvas.height-35, 5, this.colors.ground);
	this.objects.boxes[this.objects.boxes.length] = new Box(this.context, 590, this.context.canvas.height-30, 10, 20, this.colors.ground);
	this.objects.posts[this.objects.posts.length] = new Post(this.context, 595, this.context.canvas.height-5, 5, this.colors.ground);
	this.objects.posts[this.objects.posts.length] = new Post(this.context, 805, this.context.canvas.height-35, 5, this.colors.ground);
	this.objects.boxes[this.objects.boxes.length] = new Box(this.context, 800, this.context.canvas.height-30, 10, 20, this.colors.ground);
	this.objects.posts[this.objects.posts.length] = new Post(this.context, 805, this.context.canvas.height-5, 5, this.colors.ground);
	this.objects.pits[this.objects.pits.length] = new Box(this.context, 810, this.context.canvas.height-40, 750, 30, this.colors.pin);
	this.objects.boxes[this.objects.boxes.length] = new Box(this.context, 810, this.context.canvas.height-10, 90, 10, this.colors.ground);
    }
    incrementScore(amount) {
	score.value = parseInt(score.value)+amount;
    }
    incrementEnergy(accel) {
	energy.value = parseFloat(energy.value)+accel;
    }
    birth() {
	var temp = new Ball(this.context, this.context.canvas.width/2, 10, 10);
	temp.dx = 0;
	temp.dy = 1;
	this.objects.balls[this.objects.balls.length] = temp;
    }
    reset() {
	this.birth();
    }
}






var slider = document.getElementById("kappenball-stochasticity");
var score = document.getElementById("kappenball-score");
var ballCount = document.getElementById("kappenball-count");
var energy = document.getElementById("kappenball-energy");

score.value = 0
ballCount.value = 0
energy.value = 0

var newballButton = document.getElementById("kappenball-newball");
var pauseButton = document.getElementById("kappenball-pause");

newballButton.addEventListener("click", function() {
    kappenball.reset()
});
pauseButton.addEventListener("click", function() {
    kappenball.togglePause()
});

document.addEventListener("keydown", function() {
     keyDownHandler(event, kappenball);
});
document.addEventListener("keyup", function() {
    keyUpHandler(event, kappenball);
});




// Update the current slider value (each time you drag the slider handle)
var stochasticity=slider.value
slider.oninput = function() {
    kappenball.params.stochasticity=this.value;
}

var colors = {
    ground: 'rgba(56, 256, 56, 0.8)',
    pin: 'rgba(256, 56, 56, 0.8)',
    ball: 'rgba(200, 200, 200, 0.8)',
    membrane: 'rgba(56, 256, 56, 0.8)',
    hot: 'rgba(256, 56, 56, 0.8)',
    cold: 'rgba(56, 56, 256, 0.8)'
};


var simulation = {
    paused: false,
    gravity: true,
    drag: true,
    sound: false,
    clearCanv: true,
    bigBalls: false,
    dt: 1
};

var boundaries = {
    wallBounce: true,
    floorBounce: false,
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
    dragFactor: 0.97
};

var objects = {
    balls: [],
    boxes: [],
    pits: [],
    posts: [],
    membranes: []
};

var context = {
    canvas: document.getElementById("kappenball-canvas")

};

kappenball = new Kappenball(objects, params, simulation, boundaries, context, colors);

function clickReporter(event, game) {
    const rect = game.context.canvas.getBoundingClientRect()
    const x = event.clientX - rect.left
    if(x > game.context.canvas.width/2) {
	game.pushLeft(2.0)
    } else {
	game.pushRight(2.0)
    }
}


kappenball.context.canvas.addEventListener("click", function(event) {
    clickReporter(event, kappenball);
});

kappenball.reset();
draw(kappenball);
