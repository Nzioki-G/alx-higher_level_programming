#!/usr/bin/node
// print 1st arguement passed
const argv = process.argv;

if (argv[2]) {
  console.log(argv[2]);
} else {
  console.log('No argument');
}
