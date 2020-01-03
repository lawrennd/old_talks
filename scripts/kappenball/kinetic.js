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

var canvas = document.getElementById("myCanvas");
var ctx = canvas.getContext("2d");

var objArray = [];
var paused = false;
var totalKineticEnergy = 0;
var bumped = false;

var leftHeld = false;
var upHeld = false;
var rightHeld = false;
var downHeld = false;

var beep = new Audio('beep');
beep.volume = 0.002

var gravityOn = false;
var dragOn = true;
var soundOn = true;

var clearCanv = true;

var bigBalls = false;

document.addEventListener("keydown", keyDownHandler);
document.addEventListener("keyup", keyUpHandler);

function clearCanvas() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
}

function keyDownHandler(event) {
    if (event.keyCode == 67) { // c
        objArray[objArray.length] = new Ball(randomX(), randomY(), randomRadius());
    } else if (event.keyCode == 80) { // p
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
        objArray = [];
    } else if (event.keyCode == 75) { // k
        clearCanv = !clearCanv;
    } else if (event.keyCode == 88) { // x
        bigBalls = !bigBalls;
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
    }
}

function arrowControls() {
    if (leftHeld) { // left arrow
        for (var obj in objArray) {
            objArray[obj].dx -= 0.3;
        }
    } if (upHeld) { // up arrow
        for (var obj in objArray) {
            objArray[obj].dy -= 0.3;
        }
    } if (rightHeld) { // right arrow
        for (var obj in objArray) {
            objArray[obj].dx += 0.3;
        }
    } if (downHeld) { // down arrow
        for (var obj in objArray) {
            objArray[obj].dy += 0.3;
        }
    }
}

function canvasBackground() {
    canvas.style.backgroundColor = "rgb(215, 235, 240)";
}

function wallCollision(ball) {
    if (ball.x - ball.radius + ball.dx < 0 ||
        ball.x + ball.radius + ball.dx > canvas.width) {
        ball.dx *= -1;
    }
    if (ball.y - ball.radius + ball.dy < 0 ||
        ball.y + ball.radius + ball.dy > canvas.height) {
        ball.dy *= -1;
    }
    if (ball.y + ball.radius > canvas.height) {
        ball.y = canvas.height - ball.radius;
    }
    if (ball.y - ball.radius < 0) {
        ball.y = ball.radius;
    }
    if (ball.x + ball.radius > canvas.width) {
        ball.x = canvas.width - ball.radius;
    }
    if (ball.x - ball.radius < 0) {
        ball.x = ball.radius;
    }    
}

function ballCollision() {
    for (var obj1 in objArray) {
        for (var obj2 in objArray) {
            if (obj1 !== obj2 && distanceNextFrame(objArray[obj1], objArray[obj2]) <= 0) {
                var theta1 = objArray[obj1].angle();
                var theta2 = objArray[obj2].angle();
                var phi = Math.atan2(objArray[obj2].y - objArray[obj1].y, objArray[obj2].x - objArray[obj1].x);
                var m1 = objArray[obj1].mass;
                var m2 = objArray[obj2].mass;
                var v1 = objArray[obj1].speed();
                var v2 = objArray[obj2].speed();

                var dx1F = (v1 * Math.cos(theta1 - phi) * (m1-m2) + 2*m2*v2*Math.cos(theta2 - phi)) / (m1+m2) * Math.cos(phi) + v1*Math.sin(theta1-phi) * Math.cos(phi+Math.PI/2);
                var dy1F = (v1 * Math.cos(theta1 - phi) * (m1-m2) + 2*m2*v2*Math.cos(theta2 - phi)) / (m1+m2) * Math.sin(phi) + v1*Math.sin(theta1-phi) * Math.sin(phi+Math.PI/2);
                var dx2F = (v2 * Math.cos(theta2 - phi) * (m2-m1) + 2*m1*v1*Math.cos(theta1 - phi)) / (m1+m2) * Math.cos(phi) + v2*Math.sin(theta2-phi) * Math.cos(phi+Math.PI/2);
                var dy2F = (v2 * Math.cos(theta2 - phi) * (m2-m1) + 2*m1*v1*Math.cos(theta1 - phi)) / (m1+m2) * Math.sin(phi) + v2*Math.sin(theta2-phi) * Math.sin(phi+Math.PI/2);

                objArray[obj1].dx = dx1F;                
                objArray[obj1].dy = dy1F;                
                objArray[obj2].dx = dx2F;                
                objArray[obj2].dy = dy2F;
                
                if (soundOn)
                    beep.play();
            }            
        }
        wallCollision(objArray[obj1]);
    }
}

function staticCollision() {
    for (var obj1 in objArray) {
        for (var obj2 in objArray) {
            if (obj1 !== obj2 &&
                distance(objArray[obj1], objArray[obj2]) < objArray[obj1].radius + objArray[obj2].radius)
            {
                var theta = Math.atan2((objArray[obj1].y - objArray[obj2].y), (objArray[obj1].x - objArray[obj2].x));
                var overlap = objArray[obj1].radius + objArray[obj2].radius - distance (objArray[obj1], objArray[obj2]);
                var smallerObject = objArray[obj1].radius < objArray[obj2].radius ? obj1 : obj2
                objArray[smallerObject].x -= overlap * Math.cos(theta);
                objArray[smallerObject].y -= overlap * Math.sin(theta);
            }
        }
    }
}

function applyGravity() {
    for (var obj in objArray) {
        if (objArray[obj].onGround() == false) {
            objArray[obj].dy += 0.29;
        }   
    }
}

function applyDrag() {
    for (var obj in objArray) {
        objArray[obj].dx *= 0.99
        objArray[obj].dy *= 0.99
    }
}

function moveObjects() {
    for (var obj in objArray) {
        objArray[obj].x += objArray[obj].dx;
        objArray[obj].y += objArray[obj].dy;
    }    
}

function drawObjects() {
    for (var obj in objArray) {
        objArray[obj].draw();
    }
}

function draw() {

    if(clearCanv) clearCanvas();
    canvasBackground();

    if (!paused) {
        arrowControls();
        if (gravityOn) {
            applyGravity();
            applyDrag();
        }
        moveObjects();
    }

    drawObjects();
    staticCollision();
    ballCollision();
    //logger();
    requestAnimationFrame(draw);
}

function logger() {
    //log some stuff
}

// spawn the initial small thingies.
for (i = 0; i<160; i++) {
    objArray[objArray.length] = new Ball(randomX(), randomY(), randomRadius());
}

bigBalls = true;

// manually spawn the few large ones that
// start with no velocity. because i'm lazy.
for (i = 0; i<30; i++) {
    var temp = new Ball(randomX(), randomY(), randomRadius());
    temp.dx = 0;
    temp.dy = 0;
    objArray[objArray.length] = temp;
}

// and manually spawn one large ball WITH initial velocity.
// just to impart some more initial energy in the system.
objArray[objArray.length] = new Ball(randomX(), randomY(), 15);

draw();
