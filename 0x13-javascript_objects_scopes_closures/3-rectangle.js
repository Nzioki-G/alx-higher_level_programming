#!/usr/bin/node
// prints constructed rectangle
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
}
module.exports = Rectangle;
