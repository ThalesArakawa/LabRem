function setup() {
  window.addEventListener("resize", function() {
    // Resize the canvas to fill the window
    w = b.clientWidth;
    h = b.clientHeight;
  });
  myCanvas = createCanvas(w, h);
  myCanvas.parent("simulation");
  cenario = new Cenario();
  
}
function draw() {
  
  cenario.windowResponse(w, h);
  
  cenario.circle(h,circPos*10);
  cenario.rectangle(w, h);
  cenario.rectangle2(w,h);
  
  frameRate(10);

}