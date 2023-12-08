#!/usr/bin/node
// computes and prints factorial of a number
function factorial (n) {
  // base case
  if (n === 1) {
    return 1;
  }
  // recursive case
  return n * factorial(n - 1);
}

const num = process.argv[2];
if (!num) {
  console.log(1);
} else {
  console.log(factorial(parseInt(num)));
}
