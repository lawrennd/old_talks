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


var canvas = document.getElementById("multiball-canvas");
var ctx = canvas.getContext("2d");

var newballButton = document.getElementById("multiball-newball");
var pauseButton = document.getElementById("multiball-pause");

newballButton.addEventListener("click", resetGame);
pauseButton.addEventListener("click", togglePause);

var groundColor = 'rgba(56, 256, 56, 0.8)';
var pinColor = 'rgba(256, 56, 56, 0.8)';
var ballColor = 'rgba(200, 200, 200, 0.8)';


var paused = true;
var gravityOn = false;
var dragOn = false;
var soundOn = false;
var initialSpeed = 5;
var clearCanv = true;


var wallBounce = true;
var floorBounce = true;
var floorWrap = false;
var floorWrapCenter = true;
var floorReset = false;

var energy = 0.0;
var gravityAccel = 0.06;
var arrowAccel = 0.4;
var stochasticity = 0;
var stochasticityScale = 0.2;
var dragFactor = 1;

function incrementEnergy(accel) {
}

function incrementScore() {
}

function ballsBirth() {
    radius = 10;
    balls = 39;
    for (i=3*radius; i<canvas.width; i+=2*radius + 1)
    {
	var temp = new Ball(i, radius, radius);
	temp.dx = Math.random()*1e-1;
	temp.dy = initialSpeed;
	temp.color = ballColor;
	ballArray[ballArray.length] = temp;
    }
}


function resetGame() {
    ballArray = [];
    ballsBirth();
}
resetGame();

draw();
