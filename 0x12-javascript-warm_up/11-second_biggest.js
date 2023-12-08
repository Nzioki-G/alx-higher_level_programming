#!/usr/bin/node
// returns 2nd biggest integer in list
let max, max2, i;
const arr = process.argv;

max = 2;
max2 = 3;

if (arr.length <= 3) {
  console.log(0);
} else {
  for (i = 2; i < arr.length; i++) {
    if (parseInt(arr[i]) > parseInt(arr[max])) {
      max2 = max;
      max = i;
    } else if (parseInt(arr[i]) > parseInt(arr[max2]) && i !== max) {
      max2 = i;
    }
  }
  console.log(arr[max2]);
}
