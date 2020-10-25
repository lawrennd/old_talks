// This code originally written by github user miskimit and released under MIT license as below. 

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



var totalKineticEnergy = 0;

var ballArray = [];
var boxArray = [];
var postArray = [];
var pinArray = [];
var pitArray = [];

var bumped = false;

var leftHeld = false;
var upHeld = false;
var rightHeld = false;
var downHeld = false;

var beep = new Audio('beep');
beep.volume = 1


// By default inelastic collisions with no drag.
var inelasticityFactor = 1.0;
var dragFactor = 1.0;

document.addEventListener("keydown", keyDownHandler);
document.addEventListener("keyup", keyUpHandler);

function clearCanvas() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
}

function keyDownHandler(event) {
    if (event.keyCode == 67) { // c
        ballArray[ballArray.length] = new Ball(randomX(), randomY(), randomRadius());
    } else if (event.keyCode == 80) { // p
        paused = !paused;
    } else if (event.keyCode == 32) { // space bar
        paused = !paused;
    } else if (event.keyCode == 71) { // g
        gravityOn = !gravityOn;
        dragOn = !dragOn;
    } else if (event.keyCode == 77) { // m
        soundOn = !soundOn;
    } else if (event.keyCode == 65) { // A
        leftHeld = true;
    } else if (event.keyCode == 87) { // W
        upHeld = true;
    } else if (event.keyCode == 68) { // D
        rightHeld = true;
    } else if (event.keyCode == 83) { // S
        downHeld = true;
    } else if (event.keyCode == 82) { // r
        resetGame();
    } else if (event.keyCode == 75) { // k
        clearCanv = !clearCanv;
    } else if (event.keyCode == 88) { // x
        bigBalls = !bigBalls;
    } else if (event.keyCode == 37) { //left arrow
	leftHeld = true;
    } else if (event.keyCode == 39) { //right arrow
	rightHeld = true;
    }
}

function keyUpHandler(event) {
    if (event.keyCode == 65) { // A
        leftHeld = false;
    } else if (event.keyCode == 87) { // W
        upHeld = false;
    } else if (event.keyCode == 68) { // D
        rightHeld = false;
    } else if (event.keyCode == 83) { // S
        downHeld = false;
    }else if (event.keyCode == 37) { //left arrow
	leftHeld = false;
    } else if (event.keyCode == 39) { //right arrow
	rightHeld = false;
    }
}

function arrowControls() {
    if (leftHeld) { // left arrow
        for (var obj in ballArray) {
	    incrementEnergy()
            ballArray[obj].dx -= arrowAccel;
        }
    } if (upHeld) { // up arrow
        for (var obj in ballArray) {
	    incrementEnergy()
            ballArray[obj].dy -= arrowAccel;
        }
    } if (rightHeld) { // right arrow
        for (var obj in ballArray) {
	    incrementEnergy()
            ballArray[obj].dx += arrowAccel;
        }
    } if (downHeld) { // down arrow
        for (var obj in ballArray) {
	    incrementEnergy()
            ballArray[obj].dy += arrowAccel;
        }
    }
}

function canvasBackground() {
    canvas.style.backgroundColor = "rgb(215, 235, 240)";
}

function wallCollision(ball) {
    if(wallBounce)
    {
	if (ball.x - ball.radius + ball.dx < 0 ||
            ball.x + ball.radius + ball.dx > canvas.width) {
            ball.dx *= -1;
	    applyInelasticity(ball);
	}
	if (ball.x + ball.radius > canvas.width) {
            ball.x = canvas.width - ball.radius;
	}
	if (ball.x - ball.radius < 0) {
            ball.x = ball.radius;
	}
    }
}

function floorCollision(ball) {
    if(floorBounce)
    {
	if (ball.y - ball.radius + ball.dy < 0 ||
            ball.y + ball.radius + ball.dy > canvas.height) {
            ball.dy *= -1;
	    applyInelasticity(ball);
	}
	if (ball.y + ball.radius > canvas.height) {
            ball.y = canvas.height - ball.radius;
	}
	if (ball.y - ball.radius < 0) {
            ball.y = ball.radius;
	}
    }
    if(floorWrap)
    {
	if (ball.y + ball.radius + ball.dy > canvas.height) {
	    ball.y = ball.radius;
	    incrementScore();
	}
	if (ball.y - ball.radius + ball.dy < 0) {	    
	    ball.y = canvas.height-ball.radius;
	}
    }
    if(floorWrapCenter)
    {
	if (ball.y + ball.radius + ball.dy > canvas.height) {
	    ball.y = ball.radius;
	    ball.x = canvas.width/2;
	    incrementScore();
	}
	if (ball.y - ball.radius + ball.dy < 0) {	    
	    ball.y = canvas.height-ball.radius;
	    ball.x = canvas.width/2;
	}
    }
    if(floorReset)
    {
	if (ball.y + ball.radius + ball.dy > canvas.height) {
	    ball.x = canvas.width/2;
	    ball.y = ball.radius;
	    ball.dx = 0;
	}
    }
}

function collides (circle, rect, collide_inside)
{
    // From https://stackoverflow.com/questions/21089959/detecting-collision-of-rectangle-with-circle
    // compute a center-to-center vector
    var half = { x: rect.w/2, y: rect.h/2 };
    var center = {
        x: circle.x + circle.dx - (rect.x+half.x),
        y: circle.y + circle.dy - (rect.y+half.y)};

    // check circle position inside the rectangle quadrant
    var side = {
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
    var half = { x: rect.w/2, y: rect.h/2 };
    var center = {
        x: circle.x + circle.dx - (rect.x+half.x),
        y: circle.y + circle.dy - (rect.y+half.y)};

    // check circle position inside the rectangle quadrant
    var side = {
        x: Math.abs (center.x) - half.x,
        y: Math.abs (center.y) - half.y};
    if (side.x >  circle.radius || side.y >  circle.radius) // outside
        return { bounce: false }; 
    if (side.x < -circle.radius && side.y < -circle.radius) // inside
        return { bounce: false }; 
    if (side.x < 0 || side.y < 0) // intersects side or corner
    {
        var dx = 0, dy = 0;
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
    var norm = Math.sqrt (side.x*side.x+side.y*side.y);
    var dx = center.x < 0 ? -1 : 1;
    var dy = center.y < 0 ? -1 : 1;
    return { bounce:true, x: dx*side.x/norm, y: dy*side.y/norm };   
}

function boxCollision() {
    for (var obj1 in ballArray) {
	for (var obj2 in boxArray) {
	    
	    if(collides(ballArray[obj1], boxArray[obj2], true))
	    {
		var vec = bounces(ballArray[obj1], boxArray[obj2]);
		var d = {x: ballArray[obj1].dx,
			 y: ballArray[obj1].dy};
		var dn = d.x*vec.x + d.y*vec.y;
		ballArray[obj1].dx -= 2*dn*vec.x;
		ballArray[obj1].dy -= 2*dn*vec.y;
		applyInelasticity(ballArray[obj1]);
	    }
	}
    }
}


function Collision() {
    for (var obj1 in ballArray) {
	for (var obj2 in boxArray) {
	    
	    if(collides(ballArray[obj1], boxArray[obj2], false))
	    {
		var vec = bounces(ballArray[obj1], boxArray[obj2]);
		var d = {x: ballArray[obj1].dx,
			 y: ballArray[obj1].dy};
		var dn = d.x*vec.x + d.y*vec.y;
		ballArray[obj1].dx -= 2*dn*vec.x;
		ballArray[obj1].dy -= 2*dn*vec.y;
		applyInelasticity(ballArray[obj1]);
	    }
	}
    }
}

function ballCollision() {
    for (var obj1 in ballArray) {
        for (var obj2 in ballArray) {
            if (obj1 !== obj2 && distanceNextFrame(ballArray[obj1], ballArray[obj2]) <= 0) {
                var theta1 = ballArray[obj1].angle();
                var theta2 = ballArray[obj2].angle();
                var phi = Math.atan2(ballArray[obj2].y - ballArray[obj1].y, ballArray[obj2].x - ballArray[obj1].x);
                var m1 = ballArray[obj1].mass;
                var m2 = ballArray[obj2].mass;
                var v1 = ballArray[obj1].speed();
                var v2 = ballArray[obj2].speed();

                var dx1F = (v1 * Math.cos(theta1 - phi) * (m1-m2) + 2*m2*v2*Math.cos(theta2 - phi)) / (m1+m2) * Math.cos(phi) + v1*Math.sin(theta1-phi) * Math.cos(phi+Math.PI/2);
                var dy1F = (v1 * Math.cos(theta1 - phi) * (m1-m2) + 2*m2*v2*Math.cos(theta2 - phi)) / (m1+m2) * Math.sin(phi) + v1*Math.sin(theta1-phi) * Math.sin(phi+Math.PI/2);
                var dx2F = (v2 * Math.cos(theta2 - phi) * (m2-m1) + 2*m1*v1*Math.cos(theta1 - phi)) / (m1+m2) * Math.cos(phi) + v2*Math.sin(theta2-phi) * Math.cos(phi+Math.PI/2);
                var dy2F = (v2 * Math.cos(theta2 - phi) * (m2-m1) + 2*m1*v1*Math.cos(theta1 - phi)) / (m1+m2) * Math.sin(phi) + v2*Math.sin(theta2-phi) * Math.sin(phi+Math.PI/2);

                ballArray[obj1].dx = dx1F;                
                ballArray[obj1].dy = dy1F;                
                ballArray[obj2].dx = dx2F;                
                ballArray[obj2].dy = dy2F;
		applyInelasticity(ballArray[obj1]);
		applyInelasticity(ballArray[obj2]);
                if (soundOn)
                    beep.play();
            }            
        }
        wallCollision(ballArray[obj1]);
        floorCollision(ballArray[obj1]);
    }
}


function postCollision() {
    for (var obj1 in ballArray) {
        for (var obj2 in postArray) {
            if (distanceNextFrame(ballArray[obj1], postArray[obj2]) <= 0) {
                var theta1 = ballArray[obj1].angle();
                var theta2 = postArray[obj2].angle();
                var phi = Math.atan2(postArray[obj2].y - ballArray[obj1].y, postArray[obj2].x - ballArray[obj1].x);
                var m1 = ballArray[obj1].mass;
                var m2 = postArray[obj2].mass;
                var v1 = ballArray[obj1].speed();
                var v2 = postArray[obj2].speed()

                var dx1F = (v1 * Math.cos(theta1 - phi) * (m1-m2) + 2*m2*v2*Math.cos(theta2 - phi)) / (m1+m2) * Math.cos(phi) + v1*Math.sin(theta1-phi) * Math.cos(phi+Math.PI/2);
                var dy1F = (v1 * Math.cos(theta1 - phi) * (m1-m2) + 2*m2*v2*Math.cos(theta2 - phi)) / (m1+m2) * Math.sin(phi) + v1*Math.sin(theta1-phi) * Math.sin(phi+Math.PI/2);

                ballArray[obj1].dx = dx1F;                
                ballArray[obj1].dy = dy1F;                
		applyInelasticity(ballArray[obj1]);
                
                if (soundOn)
                    beep.play();
            }            
        }
    }
}

function pinCollision() {
    for (var obj2 in pinArray) {
	for (var obj1 in ballArray) {
            if (distanceNextFrame(ballArray[obj1], pinArray[obj2]) <= 0) {
		ballDie(obj1);
                if (soundOn)
                    beep.play();
		break;
            }            
        }
    }
}

function pitCollision() {
    for (var obj2 in pitArray) {   
	for (var obj1 in ballArray) {
	    if(collides(ballArray[obj1], pitArray[obj2], true))
	    {
		ballDie(obj1);
		break;
	    }
	}
    }
}


function staticCollision() {
    for (var obj1 in ballArray) {
        for (var obj2 in ballArray) {
            if (obj1 !== obj2 &&
                distance(ballArray[obj1], ballArray[obj2]) < ballArray[obj1].radius + ballArray[obj2].radius)
            {
                var theta = Math.atan2((ballArray[obj1].y - ballArray[obj2].y), (ballArray[obj1].x - ballArray[obj2].x));
                var overlap = ballArray[obj1].radius + ballArray[obj2].radius - distance (ballArray[obj1], ballArray[obj2]);
                var smallerObject = ballArray[obj1].radius < ballArray[obj2].radius ? obj1 : obj2
                ballArray[smallerObject].x -= overlap * Math.cos(theta);
                ballArray[smallerObject].y -= overlap * Math.sin(theta);
            }
        }
    }
}

function applyGravity() {
    for (var obj in ballArray) {
        if (ballArray[obj].onGround() == false) {
            ballArray[obj].dy += gravityAccel;
        }   
    }
}

function applyDrag() {
    for (var obj in ballArray) {
        ballArray[obj].dx *= dragFactor
        ballArray[obj].dy *= dragFactor
    }
}

function applyHorizontalDrag() {
    for (var obj in ballArray) {
        ballArray[obj].dx *= dragFactor
    }
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

function applyDiffusion() {
    for (var obj in ballArray) {
        ballArray[obj].dx += diffuseRandom(stochasticityScale*stochasticity);
    }
}

function applyInelasticity(ball) {
    ball.dx *= inelasticityFactor;
    ball.dy *= inelasticityFactor;
}
    

function moveObjects() {
    for (var obj in ballArray) {
        ballArray[obj].x += ballArray[obj].dx;
        ballArray[obj].y += ballArray[obj].dy;
    }    
}

function drawObjects() {
    for (var obj in ballArray) {
        ballArray[obj].draw();
    }
    for (var obj in postArray) {
        postArray[obj].draw();
    }
    for (var obj in boxArray) {
        boxArray[obj].draw();
    }
    for (var obj in pitArray) {
        pitArray[obj].draw();
    }
    for (var obj in pinArray) {
        pinArray[obj].draw();
    }
}

function draw() {

    if(clearCanv) clearCanvas();
    canvasBackground();

    if (!paused) {
	//applyHorizontalDrag();
        moveObjects();
	applyDiffusion();
        arrowControls();
        if (gravityOn) {
            applyGravity();
            applyDrag();
        }
    }

    drawObjects();
    staticCollision();
    ballCollision();
    postCollision();
    boxCollision();
    pinCollision();
    pitCollision();
    //logger();
    requestAnimationFrame(draw);
}

function logger() {
    //log some stuff
}

