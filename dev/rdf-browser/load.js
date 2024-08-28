const canvas = document.querySelector('canvas');
const context = canvas.getContext('2d');

var nodes = [];

function resize() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
}

window.onresize = resize;
resize();

function drawNode(node) {
    context.beginPath();
    context.fillStyle = node.fillStyle;
    context.arc(node.x, node.y, node.radius, 0, Math.PI * 2, true);
    context.strokeStyle = node.strokeStyle;
    context.stroke();
    context.fill();
}

function click(e) {
    let node = {
        x: e.x,
        y: e.y,
        radius: 10,
        fillStyle: '#22cccc',
        strokeStyle: '#009999'
    };
    nodes.push(node);
    draw();
}


window.onclick = click;

var selection = undefined;

function within(x, y) {
    return nodes.find(n => {
        return x > (n.x - n.radius) && 
            y > (n.y - n.radius) &&
            x < (n.x + n.radius) &&
            y < (n.y + n.radius);
    });
}

function move(e) {
    if (selection) {
        selection.x = e.x;
        selection.y = e.y;
        draw();
    }
}

function down(e) {
    let target = within(e.x, e.y);
    if (target) {
        selection = target;
    }
}

function up(e) {
    selection = undefined;
}

window.onmousemove = move;
window.onmousedown = down;
window.onmouseup = up;

function draw() {
    context.clearRect(0, 0, window.innerWidth, window.innerHeight);
    for (let i = 0; i < nodes.length; i++) {
        let node = nodes[i];
        context.beginPath();
        context.fillStyle = node.fillStyle;
        context.arc(node.x, node.y, node.radius, 0, Math.PI * 2, true);
        context.strokeStyle = node.strokeStyle;
        context.fill();
        context.stroke();
    }
}


