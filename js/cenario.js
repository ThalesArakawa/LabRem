class Cenario {
  constructor() {
    this.w;
    this.h;
  }
  windowResponse(w, h) {
    print(w,h)
      this.w = w;
      this.h = h;
    resizeCanvas(this.w, this.h);
  }
  
  circle(h,x) {
    fill(0, 204, 0);
    circle(this.w*0.1, this.h-x-this.w*0.05, this.w*0.1);
  }
  
  rectangle(w,h){
    fill(255, 204, 0);
    rect(0, 0, this.w*0.05,this.h);
  }

  rectangle2(w,h){
    fill(255, 204, 153);
    rect(this.w*0.05, 0, this.w*0.1,this.h*0.025);
  }
  
  
  
}