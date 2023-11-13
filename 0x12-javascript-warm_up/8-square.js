#!/usr/bin/node
const number = parseInt(process.argv[2]);
if (isNaN(number)) {
  console.log('Missing size');
} else {
  sq = '';
  for (i = 0; i < number; i++) {
    sq += 'X';
  }
  for (i = 0; i < number; i++) {
    console.log(sq);
  }
}
