var canvas, ctx, flag = false, prevX = 0, currX = 0, prevY = 0, currY = 0, dot_flag = false;
	
var x = "black", y = 2;
	    
function init() {
    canvas = document.getElementById('drawCanvas');
    canvas.setAttribute('width', canvas.parentNode.offsetWidth);
    canvas.setAttribute('height', canvas.parentNode.offsetHeight);
    ctx = canvas.getContext("2d");
    w = ctx.clientWidth;
    h = ctx.clientHeight;
    
    canvas.addEventListener("mousemove", function (e) {
	findxy('move', e)
    }, false);
    canvas.addEventListener("mousedown", function (e) {
	findxy('down', e)
    }, false);
    canvas.addEventListener("mouseup", function (e) {
	findxy('up', e)
    }, false);
    canvas.addEventListener("mouseout", function (e) {
	findxy('out', e)
    }, false);
}

function draw() {
    ctx.beginPath();
    ctx.moveTo(prevX, prevY);
    ctx.lineTo(currX, currY);
    ctx.strokeStyle = x;
    ctx.lineWidth = y;
    ctx.stroke();
    ctx.closePath();
}

function findxy(res, e) {
    if (res == 'down') {
	prevX = currX;
	prevY = currY;
        var cRect = canvas.getBoundingClientRect();
	currX = e.clientX - cRect.offsetLeft;
	currY = e.clientY - cRect.offsetTop;
	
	flag = true;
	dot_flag = true;
	if (dot_flag) {
	    ctx.beginPath();
	    ctx.fillStyle = x;
	    ctx.fillRect(currX, currY, 2, 2);
	    ctx.closePath();
	    dot_flag = false;
	}
    }
    if (res == 'up' || res == "out") {
	flag = false;
    }
    if (res == 'move') {
	if (flag) {
	    prevX = currX;
	    prevY = currY;
	    currX = e.clientX - canvas.offsetLeft;
	                currY = e.clientY - canvas.offsetTop;
	    draw();
	}
    }
}
init();
