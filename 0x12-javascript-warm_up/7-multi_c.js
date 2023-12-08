#!/usr/bin/node
// 'C is fun' * x
const arg1 = process.argv[2];
let i = 0;

if (arg1 === undefined) {
  console.log('Missing number of occurrences');
} else {
  parseInt(arg1);
  for (i = 0; i < arg1; i++) {
    console.log('C is fun');
  }
}
