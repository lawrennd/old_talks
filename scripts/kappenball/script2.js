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

function randomColor() {
    red = Math.floor(Math.random() * 3) * 127;
    green = Math.floor(Math.random() * 3) * 127;
    blue = Math.floor(Math.random() * 3) * 127;
    rc = "rgb(" + red + ", " + green + ", " + blue + ")";
    return rc;
}

function randomX() {
    x = Math.floor(Math.random() * canvas.width);
    if (x < 30) {
        x = 30;
    } else if (x + 30 > canvas.width) {
        x = canvas.width - 30;
    }
    return x;
}

function randomY() {
    y = Math.floor(Math.random() * canvas.height);
    if (y < 30) {
        y = 30;
    } else if (y + 30 > canvas.height) {
        y = canvas.height - 30;
    }
    return y;
}

function randomRadius() {
    if (bigBalls) {
        r = Math.ceil(Math.random() * 10 + 13);
        return r;
    } else {
        r = Math.ceil(Math.random() * 2 + 1);
        //r = 2;
        return r;
    }
}

function randomDx() {
    r = Math.floor(Math.random() * 10 - 5);
    return r;
}

function randomDy() {
    r = Math.floor(Math.random() * 10 - 5);
    return r;
}

function distanceNextFrame(a, b) {
    return Math.sqrt((a.x + a.dx - b.x - b.dx)**2 + (a.y + a.dy - b.y - b.dy)**2) - a.radius - b.radius;
}

function distance(a, b) {
    return Math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2);
}
