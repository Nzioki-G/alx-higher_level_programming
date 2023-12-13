#!/usr/bin/node
// rotates & doubles constructed rectangle
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print (params) {
    let across, row, col;
    for (row = 0; row < this.height; row++) {
      across = '';
      for (col = 0; col < this.width; col++) {
        across += 'X';
      }
      console.log(across);
    }
  }

  rotate () {
    const tmp = this.height;
    this.height = this.width;
    this.width = tmp;
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }
}
module.exports = Rectangle;
