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

