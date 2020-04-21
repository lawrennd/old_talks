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

var canvas = document.getElementById("pinballCanvas");
var ctx = canvas.getContext("2d");

var ballCount = document.getElementById("ballCountBox");
var energy = document.getElementById("energyBox");

ballCount.value = 0
energy.value = 0

var inelasticityFactor = 0.5;

var paused = false;
var gravityOn = true;
var dragOn = true;
var soundOn = false;

var stochasticity=0;

var clearCanv = true;

var ballRadius = 25;
var bigBalls = false;
var wallBounce = true;
var floorBounce = false;
var floorWrap = true;
var floorReset = false;

var yesColor = 'rgba(256, 10, 10, 0.8)';
var noColor = 'rgba(10, 10, 10, 0.8)';
var postColor = 'rgba(156, 156, 156, 0.8)';

var holeWidth = 100;
var gravityAccel = 0.06;
var arrowAccel = 0.4;
var stochasticityScale = 0.2;
var dragFactor = 1.0

function ballDie(obj) {
    ballArray.splice(obj, 1);
    ballCount.value = parseInt(ballCount.value)-1
}
function incrementScore() {
    score.value = parseInt(score.value)+10
}
function incrementEnergy() {
    energy.value = parseFloat(energy.value)+0.1;
}
function ballBirth(radius) {
    var ball = new Ball(Math.random()*canvas.width, radius, radius);
    ball.dx = 0;
    ball.dy = 1;
    if (ball.x < canvas.width/3) 
	ball.color = yesColor;
    else if (ball.x > 2*canvas.width/3) 
	ball.color = yesColor;
    else
	ball.color = noColor;
	
    ballArray[ballArray.length] = ball;
}

function addPostRow(height, start, stop, number) {
    gap = (stop - start)/(number-1);
    for(i=0; i<number; i++) {
	postArray[postArray.length] = new Post(start + i*gap, height, 5, postColor);
    }
}

function resetGame() {
    ballBirth(ballRadius);
}
// spawn the initial small thingies.
//for (i = 0; i<100; i++) {
//    ballArray[ballArray.length] = new Ball(randomX(), randomY(), 2);
//}


// manually spawn the few large ones that
// start with no velocity. because i'm lazy.

postArray[postArray.length] = new Post(5, canvas.height-35, 5, yesColor);
boxArray[boxArray.length] = new Box(0, canvas.height-30, 10, 20, yesColor);
postArray[postArray.length] = new Post(5, canvas.height-5, 5, yesColor);
boxArray[boxArray.length] = new Box(10, canvas.height-10, canvas.width/2-15, 10, yesColor);
postArray[postArray.length] = new Post(canvas.width/2-5, canvas.height-35, 5, yesColor);
boxArray[boxArray.length] = new Box(canvas.width/2-10, canvas.height-30, 10, 20, yesColor);
postArray[postArray.length] = new Post(canvas.width/2-5, canvas.height-5, 5, yesColor);
postArray[postArray.length] = new Post(canvas.width/2+5, canvas.height-35, 5, noColor);
boxArray[boxArray.length] = new Box(canvas.width/2, canvas.height-30, 10, 20, noColor);
postArray[postArray.length] = new Post(canvas.width/2+5, canvas.height-5, 5, noColor);
boxArray[boxArray.length] = new Box(canvas.width/2+10, canvas.height-10, canvas.width/2-15, 10, noColor);
postArray[postArray.length] = new Post(canvas.width-5, canvas.height-35, 5, noColor);
boxArray[boxArray.length] = new Box(canvas.width-10, canvas.height-30, 10, 20, noColor);
postArray[postArray.length] = new Post(canvas.width-5, canvas.height-5, 5, noColor);

//boxArray[boxArray.length] = new Box(0, canvas.height/2, 50, 10, groundColor);

//addPostRow(150, 150, canvas.width-150, 5);
//addPostRow(250, 75, canvas.width-75, 6);
//addPostRow(350, 150, canvas.width-150, 5);

addPostRow(150, canvas.width/3+ballRadius, canvas.width/2, 3);
addPostRow(150, 2*canvas.width/3+ballRadius, canvas.width, 5);
addPostRow(250, canvas.width/3+2*ballRadius, canvas.width/2+ballRadius, 3);
addPostRow(350, canvas.width/3+ballRadius, canvas.width/2, 3);
addPostRow(350, 2*canvas.width/3+ballRadius, canvas.width, 5);
//addPostRow(350, 150, canvas.width-150, 5);


resetGame();

draw();
