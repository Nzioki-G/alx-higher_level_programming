#!/usr/bin/node
// print square with X
const size = process.argv[2];
let i = 0;
let j = 0;
let col = '';

if (size === undefined || !parseInt(size)) {
  console.log('Missing size');
} else {
  for (i = 0; i < size; i++) {
    col = '';
    for (j = 0; j < size; j++) {
      col += 'X';
    }
    console.log(col);
  }
}
