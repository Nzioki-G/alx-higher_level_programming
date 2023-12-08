#!/usr/bin/node
// print int value of 1st arguement
const argv = process.argv;

if (argv[2] && parseInt(argv[2])) {
  console.log('My number: ' + parseInt(argv[2]));
} else {
  console.log('Not a number');
}
