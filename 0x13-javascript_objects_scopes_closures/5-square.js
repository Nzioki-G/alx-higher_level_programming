#!/usr/bin/node
// creates square from rectangle
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (s) {
    super(s, s);
  }
}
module.exports = Square;
