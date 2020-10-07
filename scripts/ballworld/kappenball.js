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

var canvas = document.getElementById("kappenballCanvas");
var ctx = canvas.getContext("2d");

var slider = document.getElementById("stochasticityRange");
var score = document.getElementById("scoreBox");
var ballCount = document.getElementById("ballCountBox");
var energy = document.getElementById("energyBox");

score.value = 0
ballCount.value = 0
energy.value = 0

// Update the current slider value (each time you drag the slider handle)
var stochasticity=slider.value
slider.oninput = function() {
  stochasticity= this.value;
}

var paused = false;
var gravityOn = true;
var dragOn = true;
var soundOn = true;

var clearCanv = true;

var bigBalls = false;
var wallBounce = true;
var floorBounce = false;
var floorWrap = false;
var floorWrapCenter = true;
var floorReset = false;

var groundColor = 'rgba(56, 256, 56, 0.8)';
var pinColor = 'rgba(256, 56, 56, 0.8)';

var holeWidth = 100;
var gravityAccel = 0.06;
var arrowAccel = 0.4;
var stochasticityScale = 0.2;
var dragFactor = 0.97

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
function ballBirth() {
    var temp = new Ball(canvas.width/2, 10, 10);
    temp.dx = 0;
    temp.dy = 1;
    ballArray[ballArray.length] = temp;
}

function resetGame() {
    ballBirth();
}
// spawn the initial small thingies.
//for (i = 0; i<100; i++) {
//    ballArray[ballArray.length] = new Ball(randomX(), randomY(), 2);
//}


// manually spawn the few large ones that
// start with no velocity. because i'm lazy.

pitArray[pitArray.length] = new Box(0, canvas.height-40, 90, 30, pinColor);
boxArray[boxArray.length] = new Box(0, canvas.height-10, 90, 10, groundColor);
postArray[postArray.length] = new Post(95, canvas.height-35, 5, groundColor);
boxArray[boxArray.length] = new Box(90, canvas.height-30, 10, 20, groundColor);
postArray[postArray.length] = new Post(95, canvas.height-5, 5, groundColor);
postArray[postArray.length] = new Post(305, canvas.height-35, 5, groundColor);
boxArray[boxArray.length] = new Box(300, canvas.height-30, 10, 20, groundColor);
postArray[postArray.length] = new Post(305, canvas.height-5, 5, groundColor);
boxArray[boxArray.length] = new Box(310, canvas.height-10, 280, 10, groundColor);
pitArray[pitArray.length] = new Box(310, canvas.height-40, 280, 30, pinColor);
postArray[postArray.length] = new Post(595, canvas.height-35, 5, groundColor);
boxArray[boxArray.length] = new Box(590, canvas.height-30, 10, 20, groundColor);
postArray[postArray.length] = new Post(595, canvas.height-5, 5, groundColor);
postArray[postArray.length] = new Post(805, canvas.height-35, 5, groundColor);
boxArray[boxArray.length] = new Box(800, canvas.height-30, 10, 20, groundColor);
postArray[postArray.length] = new Post(805, canvas.height-5, 5, groundColor);
pitArray[pitArray.length] = new Box(810, canvas.height-40, 750, 30, pinColor);
boxArray[boxArray.length] = new Box(810, canvas.height-10, 90, 10, groundColor);

//boxArray[boxArray.length] = new Box(0, canvas.height/2, 50, 10, groundColor);

//for(i=40; i<canvas.width-40; i+=40) {
//     for(j=40; j<canvas.height-40; j+=40) {
// 	postArray[postArray.length] = new Post(i, j, 5, groundColor);
//     }
// }

// for(i=160; i<canvas.width-160; i+=160) {
//     for(j=40; j<canvas.height-160; j+=160) {
// 	pinArray[pinArray.length] = new Post(i, j, 5, pinColor);
//     }
// }

//boxArray[boxArray.length] = new Box(0, 900, 200);

resetGame();

draw();
