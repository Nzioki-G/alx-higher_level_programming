#!/usr/bin/node
// creates square from rectangle
const Sqr = require('./5-square');
class Square extends Sqr {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      let across, col, row;
      for (row = 0; row < this.height; row++) {
        across = '';
        for (col = 0; col < this.width; col++) {
          across += c;
        }
        console.log(across);
      }
    }
  }
}
module.exports = Square;
