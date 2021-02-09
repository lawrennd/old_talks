// Copyright (c) 2020 Neil D. Lawrence

// Based on code originally written by github user miskimit and released under MIT license as below. 

// https://github.com/miskimit/miskimit.github.io/

// MIT License

// Copyright (c) 2016 miskimit

// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:

// The above copyright notice and this permission notice shall be included in all
// copies or substantial portions of the Software.

// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
// SOFTWARE.



// By default inelastic collisions with no drag.

var beep = new Audio("data:audio/wav;base64,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qJrx4KOQjahZxWbcZgztj2c49nKmkId44S71j0c8eV9yDK6uPRzx5X18eDvjvQ6yKo9ZSS6l//8elePK/Lf//IInrOF/FvDoADYAGBMGb7FtErm5MXMlmPAJQVgWta7Zx2go+8xJ0UiCb8LHHdftWyLJE0QIAIsI+UbXu67dZMjmgDGCGl1H+vpF4NSDckSIkk7Vd+sxEhBQMRU8j/12UIRhzSaUdQ+rQU5kGeFxm+hb1oh6pWWmv3uvmReDl0UnvtapVaIzo1jZbf/pD6ElLqSX+rUmOQNpJFa/r+sa4e/pBlAABoAAAAA3CUgShLdGIxsY7AUABPRrgCABdDuQ5GC7DqPQCgbbJUAoRSUj+NIEig0YfyWUho1VBBBA//uQZB4ABZx5zfMakeAAAAmwAAAAF5F3P0w9GtAAACfAAAAAwLhMDmAYWMgVEG1U0FIGCBgXBXAtfMH10000EEEEEECUBYln03TTTdNBDZopopYvrTTdNa325mImNg3TTPV9q3pmY0xoO6bv3r00y+IDGid/9aaaZTGMuj9mpu9Mpio1dXrr5HERTZSmqU36A3CumzN/9Robv/Xx4v9ijkSRSNLQhAWumap82WRSBUqXStV/YcS+XVLnSS+WLDroqArFkMEsAS+eWmrUzrO0oEmE40RlMZ5+ODIkAyKAGUwZ3mVKmcamcJnMW26MRPgUw6j+LkhyHGVGYjSUUKNpuJUQoOIAyDvEyG8S5yfK6dhZc0Tx1KI/gviKL6qvvFs1+bWtaz58uUNnryq6kt5RzOCkPWlVqVX2a/EEBUdU1KrXLf40GoiiFXK///qpoiDXrOgqDR38JB0bw7SoL+ZB9o1RCkQjQ2CBYZKd/+VJxZRRZlqSkKiws0WFxUyCwsKiMy7hUVFhIaCrNQsKkTIsLivwKKigsj8XYlwt/WKi2N4d//uQRCSAAjURNIHpMZBGYiaQPSYyAAABLAAAAAAAACWAAAAApUF/Mg+0aohSIRobBAsMlO//Kk4soosy1JSFRYWaLC4qZBYWFRGZdwqKiwkNBVmoWFSJkWFxX4FFRQWR+LsS4W/rFRb/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////VEFHAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAU291bmRib3kuZGUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMjAwNGh0dHA6Ly93d3cuc291bmRib3kuZGUAAAAAAAAAACU=");  
beep.volume = 1




function keyDownHandler(event, game) {
    if (event.keyCode == 67) { // c
        game.objects.balls[game.objects.balls.length] = new Ball(game.context, randomX(game), randomY(game), randomRadius(game));
    } else if (event.keyCode == 80) { // p
        game.togglePause();
    } else if (event.keyCode == 32) { // space bar
        game.togglePause();
    } else if (event.keyCode == 71) { // g
        game.simulation.gravity = !game.simulation.gravity;
        game.simulation.drag = !game.simulation.drag;
    } else if (event.keyCode == 77) { // m
        game.simulation.sound = !game.simulation.sound;
    } else if (event.keyCode == 65) { // A
        game.context.leftHeld = true;
    } else if (event.keyCode == 87) { // W
        game.context.upHeld = true;
    } else if (event.keyCode == 68) { // D
        game.context.rightHeld = true;
    } else if (event.keyCode == 83) { // S
        game.context.downHeld = true;
    } else if (event.keyCode == 82) { // r
        game.reset();
    } else if (event.keyCode == 75) { // k
        game.simulation.clearCanv = !game.simulation.clearCanv;
    } else if (event.keyCode == 88) { // x
        game.simulation.bigBalls = !game.simulation.bigBalls;
    } else if (event.keyCode == 37) { //left arrow
	game.context.leftHeld = true;
    } else if (event.keyCode == 39) { //right arrow
	game.context.rightHeld = true;
    }
}

function keyUpHandler(event, game) {
    if (event.keyCode == 65) { // A
        game.context.leftHeld = false;
    } else if (event.keyCode == 87) { // W
        game.context.upHeld = false;
    } else if (event.keyCode == 68) { // D
        game.context.rightHeld = false;
    } else if (event.keyCode == 83) { // S
        game.context.downHeld = false;
    }else if (event.keyCode == 37) { //left arrow
	game.context.leftHeld = false;
    } else if (event.keyCode == 39) { //right arrow
	game.context.rightHeld = false;
    }
}


function randomColor() {
    let red = Math.floor(Math.random() * 3) * 127;
    let green = Math.floor(Math.random() * 3) * 127;
    let blue = Math.floor(Math.random() * 3) * 127;

    let rc = "rgb(" + red + ", " + green + ", " + blue + ")";
    return rc;
}

function randomX(game) {
    let x = Math.floor(Math.random() * game.context.canvas.width);
    if (x < 30) {
        x = 30;
    } else if (x + 30 > game.context.canvas.width) {
        x = game.context.canvas.width - 30;
    }
    return x;
}

function randomY(game) {
    let y = Math.floor(Math.random() * game.context.canvas.height);
    if (y < 30) {
        y = 30;
    } else if (y + 30 > game.context.canvas.height) {
        y = game.context.canvas.height - 30;
    }
    return y;
}

function randomRadius(game) {
    if (game.simulation.bigBalls) {
        let r = Math.ceil(Math.random() * 10 + 20);
        return r;
    } else {
        let r = Math.ceil(Math.random() * 2 + 2);
        return r;
    }
}

function randomDx(game) {
    let r = Math.floor(Math.random() * 10 - 5);
    return r;
}

function randomDy(game) {
    let r = Math.floor(Math.random() * 10 - 5);
    return r;
}

function Ball(context, x, y, radius) {
    this.radius = radius;
    this.dx = randomDx();
    this.dy = randomDy();
    // mass is that of a sphere as opposed to circle.
    // it *does* make a difference.
    this.mass = this.radius * this.radius * this.radius;
    this.x = x;
    this.y = y;
    this.color = randomColor();
    this.draw = function() {
        context.ctx.beginPath();
        context.ctx.arc(Math.round(this.x), Math.round(this.y), this.radius, 0, 2*Math.PI);
        context.ctx.fillStyle = this.color;
        context.ctx.fill();
        context.ctx.strokeStyle = 'rgba(0, 0, 0, 0.6)';
        context.ctx.stroke();
        context.ctx.closePath();
    };
    this.speed = function() {
        // magnitude of velocity vector
        return Math.sqrt(this.dx * this.dx + this.dy * this.dy);
    };
    this.angle = function() {
        //angle of ball with the x axis
        return Math.atan2(this.dy, this.dx);
    };
    this.kineticEnergy = function () {
    // only for masturbation purposes, not rly used for computation.
        return (0.5 * this.mass * this.speed() * this.speed());
    };
    this.onGround = function() {
        return (this.y + this.radius >= context.canvas.height)
    }
}

function Post(context, x, y, radius, color) {
    this.radius = radius;
    this.dx = 0;
    this.dy = 0;
    // mass is that of a sphere as opposed to circle.
    // it *does* make a difference.
    this.mass = 2e9;
    this.x = x;
    this.y = y;
    this.color = color;
    this.draw = function() {
        context.ctx.beginPath();
        context.ctx.arc(Math.round(this.x), Math.round(this.y), this.radius, 0, 2*Math.PI);
        context.ctx.fillStyle = this.color;
        context.ctx.fill();
        context.ctx.strokeStyle = 'rgba(0, 0, 0, 0.6)';
        context.ctx.stroke();
        context.ctx.closePath();
    };
    this.speed = function() {
        // magnitude of velocity vector
        return 0;
    };
    this.angle = function() {
        //angle of ball with the x axis
        return 0;
    };
    this.kineticEnergy = function () {
    // not rly used for computation.
        return 0;
    };
}


function Box(context, x, y, w, h, color) {
    this.x = x;
    this.y = y;
    this.w = w;
    this.h = h;
    this.membraneImmune = false;
    this.color = color;
    this.draw = function() {
        context.ctx.beginPath();
	context.ctx.moveTo(x, y);
	context.ctx.lineTo(x+w, y);
	context.ctx.lineTo(x+w, y+h);
	context.ctx.lineTo(x, y+h);
	context.ctx.lineTo(x, y);
        context.ctx.fillStyle = this.color;
        context.ctx.fill();
        context.ctx.strokeStyle = 'rgba(0, 0, 0, 0.6)';
        context.ctx.stroke();
        context.ctx.closePath();
    };
}

function Membrane(context, x, y, w, h, color) {
    this.x = x;
    this.y = y;
    this.w = w;
    this.h = h;
    this.color = color;
    this.draw = function() {
        context.ctx.beginPath();
	context.ctx.moveTo(x, y);
	context.ctx.lineTo(x+w, y);
	context.ctx.lineTo(x+w, y+h);
	context.ctx.lineTo(x, y+h);
	context.ctx.lineTo(x, y);
        context.ctx.fillStyle = this.color;
        context.ctx.fill();
        context.ctx.strokeStyle = 'rgba(0, 0, 0, 0.6)';
        context.ctx.stroke();
        context.ctx.closePath();
    };
}

function Ball(context, x, y, radius) {
    this.radius = radius;
    this.dx = randomDx();
    this.dy = randomDy();
    // mass is that of a sphere as opposed to circle.
    // it *does* make a difference.
    this.mass = this.radius * this.radius * this.radius;
    this.x = x;
    this.y = y;
    this.color = randomColor(this);
    this.draw = function() {
        context.ctx.beginPath();
        context.ctx.arc(Math.round(this.x), Math.round(this.y), this.radius, 0, 2*Math.PI);
        context.ctx.fillStyle = this.color;
        context.ctx.fill();
        context.ctx.strokeStyle = 'rgba(0, 0, 0, 0.6)';
        context.ctx.stroke();
        context.ctx.closePath();
    };
    this.speed = function() {
        // magnitude of velocity vector
        return Math.sqrt(this.dx * this.dx + this.dy * this.dy);
    };
    this.angle = function() {
        //angle of ball with the x axis
        return Math.atan2(this.dy, this.dx);
    };
    this.kineticEnergy = function () {
    // only for masturbation purposes, not rly used for computation.
        return (0.5 * this.mass * this.speed() * this.speed());
    };
    this.onGround = function() {
        return (this.y + this.radius >= context.canvas.height)
    }
}

function Post(context, x, y, radius, color) {
    this.radius = radius;
    this.dx = 0;
    this.dy = 0;
    // mass is that of a sphere as opposed to circle.
    // it *does* make a difference.
    this.mass = 2e9;
    this.x = x;
    this.y = y;
    this.color = color;
    this.draw = function() {
        context.ctx.beginPath();
        context.ctx.arc(Math.round(this.x), Math.round(this.y), this.radius, 0, 2*Math.PI);
        context.ctx.fillStyle = this.color;
        context.ctx.fill();
        context.ctx.strokeStyle = 'rgba(0, 0, 0, 0.6)';
        context.ctx.stroke();
        context.ctx.closePath();
    };
    this.speed = function() {
        // magnitude of velocity vector
        return 0;
    };
    this.angle = function() {
        //angle of ball with the x axis
        return 0;
    };
    this.kineticEnergy = function () {
    // not rly used for computation.
        return 0;
    };
}


function Box(context, x, y, w, h, color) {
    this.x = x;
    this.y = y;
    this.w = w;
    this.h = h;
    this.membraneImmune = false;
    this.color = color;
    this.draw = function() {
        context.ctx.beginPath();
	context.ctx.moveTo(x, y);
	context.ctx.lineTo(x+w, y);
	context.ctx.lineTo(x+w, y+h);
	context.ctx.lineTo(x, y+h);
	context.ctx.lineTo(x, y);
        context.ctx.fillStyle = this.color;
        context.ctx.fill();
        context.ctx.strokeStyle = 'rgba(0, 0, 0, 0.6)';
        context.ctx.stroke();
        context.ctx.closePath();
    };
}

function Membrane(context, x, y, w, h, color) {
    this.x = x;
    this.y = y;
    this.w = w;
    this.h = h;
    this.color = color;
    this.draw = function() {
        context.ctx.beginPath();
	context.ctx.moveTo(x, y);
	context.ctx.lineTo(x+w, y);
	context.ctx.lineTo(x+w, y+h);
	context.ctx.lineTo(x, y+h);
	context.ctx.lineTo(x, y);
        context.ctx.fillStyle = this.color;
        context.ctx.fill();
        context.ctx.strokeStyle = 'rgba(0, 0, 0, 0.6)';
        context.ctx.stroke();
        context.ctx.closePath();
    };
}



function distanceNextFrame(a, b) {
    return Math.sqrt((a.x + a.dx - b.x - b.dx)**2 + (a.y + a.dy - b.y - b.dy)**2) - a.radius - b.radius;
}

function distance(a, b) {
    return Math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2);
}


function diffuseRandom(scale) {
    sum = 0;
    total = 10;
    for (i=0; i<total; i++)
    {
	sum+= Math.random()-0.5;
    }
    
    return scale*sum/total;
}


function collides (circle, rect, collide_inside)
{
    // From https://stackoverflow.com/questions/21089959/detecting-collision-of-rectangle-with-circle
    // compute a center-to-center vector
    let half = { x: rect.w/2, y: rect.h/2 };
    let center = {
        x: circle.x + circle.dx - (rect.x+half.x),
        y: circle.y + circle.dy - (rect.y+half.y)};

    // check circle position inside the rectangle quadrant
    let side = {
        x: Math.abs (center.x) - half.x,
        y: Math.abs (center.y) - half.y};
    if (side.x >  circle.radius || side.y >  circle.radius) {// outside
        return false;
    }
    if (side.x < -circle.radius && side.y < -circle.radius) {// inside
        return collide_inside;
    }
    if (side.x < 0 || side.y < 0) {// intersects side or corner 
        return true;
    }
    // circle is near the corner
    return side.x*side.x + side.y*side.y  < circle.radius*circle.radius;
}


function bounces (circle, rect)
{
    // From https://stackoverflow.com/questions/21089959/detecting-collision-of-rectangle-with-circle
    // compute a center-to-center vector
    let half = { x: rect.w/2, y: rect.h/2 };
    let center = {
        x: circle.x + circle.dx - (rect.x+half.x),
        y: circle.y + circle.dy - (rect.y+half.y)};

    // check circle position inside the rectangle quadrant
    let side = {
        x: Math.abs (center.x) - half.x,
        y: Math.abs (center.y) - half.y};
    if (side.x >  circle.radius || side.y >  circle.radius) // outside
        return { bounce: false }; 
    if (side.x < -circle.radius && side.y < -circle.radius) // inside
        return { bounce: false }; 
    if (side.x < 0 || side.y < 0) // intersects side or corner
    {
        let dx = 0, dy = 0;
        if (Math.abs (side.x) <= circle.radius && side.y < 0)
        {
            dx = center.x*side.x < 0 ? -1 : 1;
        }
        else if (Math.abs (side.y) <= circle.radius && side.x < 0)
        {
            dy = center.y*side.y < 0 ? -1 : 1;
        }

        return { bounce: true, x:dx, y:dy };
    }
    // circle is near the corner
    bounce = side.x*side.x + side.y*side.y  <= circle.radius*circle.radius;
    if (!bounce) return { bounce:false }
    let norm = Math.sqrt (side.x*side.x+side.y*side.y);
    let dx = center.x < 0 ? -1 : 1;
    let dy = center.y < 0 ? -1 : 1;
    return { bounce:true, x: dx*side.x/norm, y: dy*side.y/norm };   
}

function histogramSpeeds(game, canvas) {
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
    Plotly.newPlot(canvas, data, layout, {displayModeBar: false});
}

function runPhysics(game) {
    //game.horizontalDrag();
    game.move();
    game.simulation.time += game.simulation.dt;
    game.physics();
    
    // Perform global checks
    game.demon();
    
    // Check for collisions
    game.collisions()
    game.logger()    
}


const timer = ms => new Promise(res => setTimeout(res, ms))

async function draw(game) {

    if(game.simulation.clearCanv)
	game.clearCanvas();
    game.canvasBackground();
    do {
	setTimeout(runPhysics(game), 0);
    }
    while(!game.simulation.draw)

    game.draw();
    
    // fix this to use setTimeout to set timing: http://www.javascriptkit.com/javatutors/requestanimationframe.shtml
    // Add 100 millisecond delay
    do {
	await timer(10);
    }
    while(game.simulation.paused);
    
    requestAnimationFrame(function() {
        draw(game);
    });
}


class Game {
    constructor(objects, params, simulation, boundaries, context, colors) {
	this.objects = objects;
	this.simulation = simulation;
	this.params = params;
	this.boundaries = boundaries;
	this.context = context;
	this.context.ctx = this.context.canvas.getContext("2d");
	this.context.rightHeld = false;
	this.context.leftHeld = false;
	this.context.upHeld = false;
	this.context.downHeld = false;
	this.colors = colors;
	this.simulation.time = 0;
	this.simulation.draw = true;
    }

    birth() { // set up at start
    }
    reset() { // reset 
    }
    togglePause() {
	this.simulation.paused = !this.simulation.paused;
    }
    toggleDraw() {
	this.simulation.draw = !this.simulation.draw;
    }
    physics() { // apply the physics
	this.diffusion();
        this.arrowControls();
        if (this.simulation.gravity) 
            this.gravity();
	if (this.simulation.drag)
            this.drag();

    }
    diffusion() { // apply diffusion
	for (let ball in this.objects.balls) {
            this.objects.balls[ball].dx += diffuseRandom(this.params.stochasticityScale*this.params.stochasticity);
	}
    }
    drag() { // apply drag
	for (let ball in this.objects.balls) {
            this.objects.balls[ball].dx *= this.params.dragFactor
            this.objects.balls[ball].dy *= this.params.dragFactor
	}
    }
    applyInelasticity() {
    }
    horizontalDrag() {
	for (let obj in this.objects.balls) {
            this.objects.balls[obj].dx *= this.params.dragFactor
	}
    }
    gravity() { // apply gravity
	for (let obj in this.objects.balls) {
            if (this.objects.balls[obj].onGround() == false) {
		this.objects.balls[obj].dy += this.params.gravityAccel;
            }   
	}
    }
    arrowControls() {
	if (this.context.leftHeld) { // left arrow
	    this.pushLeft(this.params.arrowAccel);
	} if (this.context.upHeld) { // up arrow
	    this.pushUp(this.params.arrowAccel);
	} if (this.context.rightHeld) { // right arrow
	    this.pushRight(this.params.arrowAccel);
	} if (this.context.downHeld) { // down arrow
	    this.pushDown(this.params.arrowAccel);
	}
    }
    pushLeft(accel) {
	for (let obj in this.objects.balls) {
	    this.incrementEnergy(accel/this.objects.balls[obj].radius);
            this.objects.balls[obj].dx -= accel/this.objects.balls[obj].radius;
	}
    }
    
    pushUp(accel) {
	for (let obj in this.objects.balls) {
	    this.incrementEnergy(accel/this.objects.balls[obj].radius);
            this.objects.balls[obj].dy -= accel/this.objects.balls[obj].radius;
	}
    }
    
    pushRight(accel) {
	for (let obj in this.objects.balls) {
	    this.incrementEnergy(accel/this.objects.balls[obj].radius);
            this.objects.balls[obj].dx += accel/this.objects.balls[obj].radius;
	}
    }
    
    pushDown(accel) {
	for (let obj in this.objects.balls) {
	    this.incrementEnergy(accel/this.objects.balls[obj].radius);
	    this.objects.balls[obj].dy += accel/this.objects.balls[obj].radius;
	}
    }
    
    incrementScore(amount) {
	this.score += amount
    }
    incrementEnergy(energy) {
	this.energy += energy;
    }
    
    move() { // move the objects' locations.
	for (let obj in this.objects.balls) {
            this.objects.balls[obj].x += this.objects.balls[obj].dx*this.simulation.dt;
            this.objects.balls[obj].y += this.objects.balls[obj].dy*this.simulation.dt;
	}    
    }
    clearCanvas() {
	this.context.ctx.clearRect(0, 0, this.context.canvas.width, this.context.canvas.height);
    }
    canvasBackground() {
	this.context.canvas.style.backgroundColor = "rgb(215, 235, 240)";
    }
    demon() { // demon operations
	
    }
    logger() {
	//log some stuff
    }
    collisions() { /// do collision detection
	this.ballCollision();
	this.postCollision();
	this.boxCollision();
	this.membraneCollision();
	this.pinCollision();
	this.pitCollision();
    }
    staticCollision(ob1, ob2, emergency=false) {
	let overlap = ob1.radius + ob2.radius - distance(ob1, ob2);
	let smallerObject = ob1.radius < ob2.radius ? ob1: ob2;
	let biggerObject = ob1.radius > ob2.radius ? ob1 : ob2;

	// When things go normally, this line does not execute.
	// "Emergency" is when staticCollision has run, but the collision
	// still hasn't been resolved. Which implies that one of the objects
	// is likely being jammed against a corner, so we must now move the OTHER one instead.
	// in other words: this line basically swaps the "little guy" role, because
	// the actual little guy can't be moved away due to being blocked by the wall.
	// Neil commenting this because of jittery behaviour before Celsius lecture
	//if (emergency) [smallerObject, biggerObject] = [biggerObject, smallerObject]
	let theta = Math.atan2((biggerObject.y - smallerObject.y), (biggerObject.x - smallerObject.x));
	smallerObject.x -= overlap * Math.cos(theta);
	smallerObject.y -= overlap * Math.sin(theta); 
	
	if (distance(ob1, ob2) < ob1.radius + ob2.radius) {
            // we don't want to be stuck in an infinite emergency.
            // so if we have already run one emergency round; just ignore the problem.
            if (!emergency) this.staticCollision(ob1, ob2, true)
	}
    }
    ballCollision() {
	for (let i=0; i<this.objects.balls.length-1; i++) {
	    let ob1 = this.objects.balls[i];
            for (let j=i+1; j<this.objects.balls.length; j++) {
		let ob2 = this.objects.balls[j];
		let dist = distance(ob1, ob2);
		if(dist < ob1.radius + ob2.radius) {
                    let theta1 = ob1.angle();
                    let theta2 = ob2.angle();
                    let phi = Math.atan2(ob2.y - ob1.y, ob2.x - ob1.x);
                    let m1 = ob1.mass;
                    let m2 = ob2.mass;
                    let v1 = ob1.speed();
                    let v2 = ob2.speed();
		    
                    let dx1F = (v1 * Math.cos(theta1 - phi) * (m1-m2) + 2*m2*v2*Math.cos(theta2 - phi)) / (m1+m2) * Math.cos(phi) + v1*Math.sin(theta1-phi) * Math.cos(phi+Math.PI/2);
                    let dy1F = (v1 * Math.cos(theta1 - phi) * (m1-m2) + 2*m2*v2*Math.cos(theta2 - phi)) / (m1+m2) * Math.sin(phi) + v1*Math.sin(theta1-phi) * Math.sin(phi+Math.PI/2);
                    let dx2F = (v2 * Math.cos(theta2 - phi) * (m2-m1) + 2*m1*v1*Math.cos(theta1 - phi)) / (m1+m2) * Math.cos(phi) + v2*Math.sin(theta2-phi) * Math.cos(phi+Math.PI/2);
                    let dy2F = (v2 * Math.cos(theta2 - phi) * (m2-m1) + 2*m1*v1*Math.cos(theta1 - phi)) / (m1+m2) * Math.sin(phi) + v2*Math.sin(theta2-phi) * Math.sin(phi+Math.PI/2);
		    
                    ob1.dx = dx1F;                
                    ob1.dy = dy1F;                
                    ob2.dx = dx2F;                
                    ob2.dy = dy2F;

		    this.staticCollision(ob1, ob2);
                    if (this.params.soundOn)
			beep.play();
		}            
	    }		
	    this.wallCollision(ob1);
	    this.floorCollision(ob1);
	}
	if(this.objects.balls.length>0) {
	    this.wallCollision(this.objects.balls[this.objects.balls.length-1]);
	    this.floorCollision(this.objects.balls[this.objects.balls.length-1]);
	}
	
    }
    wallCollision(ball) {
	if(this.boundaries.wallBounce)
	{
	    if (ball.x - ball.radius + ball.dx < 0 ||
		ball.x + ball.radius + ball.dx > this.context.canvas.width) {
		ball.dx *= -1;
		this.applyInelasticity(ball, params);
	    }
	    if (ball.x + ball.radius > this.context.canvas.width) {
		ball.x = this.context.canvas.width - ball.radius;
	    }
	    if (ball.x - ball.radius < 0) {
		ball.x = ball.radius;
	    }
	}
    }

    floorCollision(ball) {
	if(this.boundaries.floorBounce)
	{
	    if (ball.y - ball.radius + ball.dy < 0 ||
		ball.y + ball.radius + ball.dy > this.context.canvas.height) {
		ball.dy *= -1;
		this.applyInelasticity(ball);
	    }
	    if (ball.y + ball.radius > this.context.canvas.height) {
		ball.y = this.context.canvas.height - ball.radius;
	    }
	    if (ball.y - ball.radius < 0) {
		ball.y = ball.radius;
	    }
	}
	if(this.boundaries.floorWrap)
	{
	    if (ball.y + ball.radius + ball.dy > this.context.canvas.height) {
		ball.y = ball.radius;
		this.incrementScore(10);
	    }
	    if (ball.y - ball.radius + ball.dy < 0) {	    
		ball.y = this.context.canvas.height-ball.radius;
	    }
	}
	if(this.boundaries.floorWrapCenter)
	{
	    if (ball.y + ball.radius + ball.dy > this.context.canvas.height) {
		ball.y = ball.radius;
		ball.x = this.context.canvas.width/2;
		this.incrementScore(10);
	    }
	    if (ball.y - ball.radius + ball.dy < 0) {	    
		ball.y = this.context.canvas.height-ball.radius;
		ball.x = this.context.canvas.width/2;
	    }
	}
	if(this.boundaries.floorReset)
	{
	    if (ball.y + ball.radius + ball.dy > this.context.canvas.height) {
		ball.x = this.context.canvas.width/2;
		ball.y = ball.radius;
		ball.dx = 0;
	    }
	}
    }
    
    postCollision() {
	for (let obj1 in this.objects.balls) {
            for (let obj2 in this.objects.posts) {
		if (distanceNextFrame(this.objects.balls[obj1], this.objects.posts[obj2]) <= 0) {
                    let theta1 = this.objects.balls[obj1].angle();
                    let theta2 = this.objects.posts[obj2].angle();
                    let phi = Math.atan2(this.objects.posts[obj2].y
					 - this.objects.balls[obj1].y,
					 this.objects.posts[obj2].x
					 - this.objects.balls[obj1].x);
                    let m1 = this.objects.balls[obj1].mass;
                    let m2 = this.objects.posts[obj2].mass;
                    let v1 = this.objects.balls[obj1].speed();
                    let v2 = this.objects.posts[obj2].speed();
		    
                    let dx1F = (v1 * Math.cos(theta1 - phi) * (m1-m2) + 2*m2*v2*Math.cos(theta2 - phi)) / (m1+m2) * Math.cos(phi) + v1*Math.sin(theta1-phi) * Math.cos(phi+Math.PI/2);
                    let dy1F = (v1 * Math.cos(theta1 - phi) * (m1-m2) + 2*m2*v2*Math.cos(theta2 - phi)) / (m1+m2) * Math.sin(phi) + v1*Math.sin(theta1-phi) * Math.sin(phi+Math.PI/2);
		    
                    this.objects.balls[obj1].dx = dx1F;                
                    this.objects.balls[obj1].dy = dy1F;                
		    this.applyInelasticity(this.objects.balls[obj1]);
                
                    if (this.params.soundOn)
			beep.play();
		}            
            }
	}
    }
    
    boxCollision() {
	for (let obj1 in this.objects.balls) {
	    for (let obj2 in this.objects.boxes) {
		
		if(collides(this.objects.balls[obj1], this.objects.boxes[obj2], true))
		{
		    let vec = bounces(this.objects.balls[obj1], this.objects.boxes[obj2]);
		    let d = {x: this.objects.balls[obj1].dx,
			     y: this.objects.balls[obj1].dy};
		    let dn = d.x*vec.x + d.y*vec.y;
		    this.objects.balls[obj1].dx -= 2*dn*vec.x;
		    this.objects.balls[obj1].dy -= 2*dn*vec.y;
		    this.applyInelasticity(this.objects.balls[obj1]);
		}
	    }
	}
    }
    
    membraneCollision() {
	for (let ball in this.objects.balls) {
	    for (let membrane in this.objects.membranes) {
		if(!this.objects.balls[ball].membraneImmune)
		{
		    if(collides(this.objects.balls[ball], this.objects.membranes[membrane], true))
		    {
			let vec = bounces(this.objects.balls[ball], this.objects.membranes[membrane]);
			let d = {x: this.objects.balls[ball].dx,
				 y: this.objects.balls[ball].dy};
			let dn = d.x*vec.x + d.y*vec.y;
			this.objects.balls[ball].dx -= 2*dn*vec.x;
			this.objects.balls[ball].dy -= 2*dn*vec.y;
			this.applyInelasticity(this.objects.balls[ball]);
		    }
		}
	    }
	}
    }
    
    pinCollision() {
	for (let pin in this.objects.pins) {
	    for (let ball in this.objects.balls) {
		if (distanceNextFrame(this.objects.balls[ball],
				      this.objects.pins[pin]) <= 0) {
		    this.ballDie(ball);
		    break;
		}            
            }
	}
    }
    
    pitCollision() {
	for (let pit in this.objects.pits) {   
	    for (let ball in this.objects.balls) {
		if(collides(this.objects.balls[ball],
			    this.objects.pits[pit], true))
		{
		    this.ballDie(ball);
		    break;
		}
	    }
	}
    }
    
    ballDie(ball) {
	this.objects.balls.splice(ball, 1);
    }

    draw() { // redraw the objects
	for (let obj in this.objects.balls) {
            this.objects.balls[obj].draw();
	}
	for (let obj in this.objects.posts) {
            this.objects.posts[obj].draw();
	}
	for (let obj in this.objects.boxes) {
            this.objects.boxes[obj].draw();
	}
	for (let obj in this.objects.membranes) {
            this.objects.membranes[obj].draw();
	}
	for (let obj in this.objects.pits) {
            this.objects.pits[obj].draw();
	}
	for (let obj in this.objects.pins) {
            this.objects.pins[obj].draw();
	}
    }   
}

class HistogramGame extends Game {
    constructor(objects, params, simulation, boundaries, context, colors, histogram) {
	super(objects, params, simulation, boundaries, context, colors);
	const step = (histogram.max-histogram.min)/histogram.nbins;
	this.histogram = {
	    nbins: histogram.nbins,
	    min: histogram.min,
	    max: histogram.max,
	    step: step,
	    y: new Array(histogram.nbins).fill(0),
	    x: new Array(histogram.nbins),
	    width: new Array(histogram.nbins).fill(step),
	    sum: 0,
	}
	for(let i=0; i<histogram.nbins; i++) {
	    this.histogram.x[i] = i*step+histogram.min;
	}
	
    }
    demon() {
	for (let i = 0; i < this.objects.balls.length; i++) {
	    let dx = this.objects.balls[i].dx-this.histogram.min;
	    let dy = this.objects.balls[i].dy-this.histogram.min;
	    for (let j=0; j<this.histogram.nbins; j++) {
		if(dx > j*this.histogram.step && dx < (j+1)*this.histogram.step) {
		    this.histogram.y[j]++;
		    this.histogram.sum++;
		    
		}
		if(dy > j*this.histogram.step && dy < (j+1)*this.histogram.step) {
		    this.histogram.y[j]++;
		    this.histogram.sum++;
		    
		}
	    }
	}
	this.entropy = 0;
	for(let i = 0; i < this.histogram.nbins; i++) {
	    if(this.histogram.y[i] > 0) {
		this.entropy -= this.histogram.y[i]/this.histogram.sum*Math.log(this.histogram.y[i]/this.histogram.sum)
	    }
	}
	if (this.simulation.time % 1000 == 0) {
	    this.simulation.draw=true;
	    
	}
    }
}
