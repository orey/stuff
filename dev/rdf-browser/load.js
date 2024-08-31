"use strict";

const canvas = document.querySelector('canvas');
const context = canvas.getContext('2d');
const globalheight = 800;
const globalwidth = 600;
let W,H;

const RelStrokeStyle =  '#009999';


//========================================Define canvas
function resize(fullscreen=false) {
    if (fullscreen) {
        W = window.innerWidth;
        H = window.innerHeight;
    }
    else {
        W = globalwidth;
        H = globalheight;
    }
    canvas.width = W;
    canvas.height = H;
}

window.onresize = resize;
resize(false);

function clearContext() {
    //context.clearRect(0, 0, window.innerWidth, window.innerHeight);
    context.clearRect(0, 0, W, H);
}


//========================================Define main structures
class Node {
    radius = 10;
    fillStyle = '#22cccc';
    strokeStyle = '#009999';
    //construct
    constructor(name,x,y){
        this.name = name
        this.x = x
        this.y = y
        console.log("New node created");
    }
    //draw
    draw(context) {
        context.beginPath();
        context.fillStyle = this.fillStyle;
        context.arc(this.x, this.y, this.radius, 0, Math.PI * 2, true);
        context.strokeStyle = this.strokeStyle;
        context.fill();
        context.stroke();
    }
}

class Rel {
    strokeStyle = RelStrokeStyle;
    constructor(name,fromNode,toNode) {
        this.name = name;
        this.fromNode = fromNode;
        this.toNode = toNode;
    }
    draw(context) {
        context.beginPath();
        context.strokeStyle = this.strokeStyle;
        context.moveTo(this.fromNode.x, this.fromNode.y);
        context.lineTo(this.toNode.x, this.toNode.y);
        context.stroke();
    }
}


// Supposed to contain all that is in the screen
class Screen {
    allnodes = [];
    allrels = [];
    pendingline = false;
    donothing=false;
    addNode(node){
        this.allnodes.push(node);
    }
    addRel(rel){
        this.allrels.push(rel);
    }
    //draw
    // The 3 last parameters are just used in case of pending line
    draw(context,selection=undefined,x=0,y=0){
        clearContext();
        for (const node of this.allnodes)
            node.draw(context);
        for (const rel of this.allrels)
            rel.draw(context);
        if (this.pendingline) {
            context.beginPath();
            context.strokeStyle = RelStrokeStyle
            context.moveTo(selection.x, selection.y);
            context.lineTo(x, y);
            context.stroke();
        }
    }
    //find
    within(x,y){
        return this.allnodes.find(n => {
            return x > (n.x - n.radius) && 
                y > (n.y - n.radius) &&
                x < (n.x + n.radius) &&
                y < (n.y + n.radius);
        })
    }
}

const myScreen = new Screen();



//===============================Drawing nodes by clicking
document.body.addEventListener('contextmenu',
                               rightclick,
                               false);


function rightclick(event) {
    event.preventDefault();
    down(event);
    //alert("event");
    return false; // needed to block the default context menu
}



//=================================Moving nodes by maintaining nodes clicked
let selection = undefined;

function move(e) {
    if (myScreen.pendingline){
        if (selection)
            myScreen.draw(context,selection,e.x,e.y);
    }
    else {
        if (selection) {
            selection.x = e.x;
            selection.y = e.y;
            myScreen.draw(context);
        }
    }
}


/*function rightclickdown(e) {
    console.log("in rightclikdown");
    console.log(e.button)
    let target = myScreen.within(e.x, e.y);
    if (target) {
        selection = target;
    }
}*/

function down(e) {
    console.log("in down");
    console.log(e.button)
    let target = myScreen.within(e.x, e.y);
    if (target) {
        selection = target;
        if (e.button == 0){
            myScreen.pendingline = true;
            return false;
        }
    }
}

function up(e) {
    console.log("in up");
    console.log(e.button) // 0 pour left et 2 pour right
    if ((selection) && (myScreen.pendingline)) {
        let stop = myScreen.within(e.x, e.y);
        //we have an object at the target
        if (stop) {
            myScreen.pendingline=false;
            myScreen.donothing=true;
            console.log(selection);
            console.log(stop);
            let rel = new Rel("rel",selection,stop);
            myScreen.addRel(rel);
            myScreen.draw(context);
        }
    }
    selection = undefined;
}

window.onmousemove = move;
window.onmousedown = down;
window.onmouseup = up;

function click(e) {
    console.log("in click");
    console.log(e.button)
    if (myScreen.donothing)
        myScreen.donothing=false;
    else {
        let node = new Node("test1", e.x, e.y)
        myScreen.addNode(node);
        myScreen.draw(context);
    }
}

window.onclick = click;







