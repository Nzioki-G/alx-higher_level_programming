#!/usr/bin/node
// print sum of args
function add (a, b) {
  return a + b;
}

const num1 = process.argv[2];
const num2 = process.argv[3];

if (num1 === undefined || num2 === undefined || !typeof num1 === 'number' || !typeof num2 === 'number') {
  console.log('NaN');
} else {
  console.log(add(parseInt(num1), parseInt(num2)));
}
