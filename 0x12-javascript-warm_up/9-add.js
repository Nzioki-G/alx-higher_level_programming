#!/usr/bin/node
function add (a, b) {
  a = parseInt(a);
  b = parseInt(b);
  return (a + b);
}
const args = process.argv;
console.log(add(args[2], args[3]));
