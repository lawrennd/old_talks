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

function keyDownHandler(event, game) {
    if (event.keyCode == 67) { // c
        game.objects.balls[game.objects.balls.length] = new Ball(randomX(), randomY(), randomRadius());
    } else if (event.keyCode == 80) { // p
        game.simulation.paused = !game.simulation.paused;
    } else if (event.keyCode == 32) { // space bar
        game.simulation.paused = !game.simulation.paused;
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
        resetGame(game);
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

