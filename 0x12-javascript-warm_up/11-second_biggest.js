#!/usr/bin/node
const arr = process.argv;
if (arr.length <= 3) {
  console.log(0);
} else {
  max = parseInt(arr[2]);
  max2 = max;

  for (i = 3; i < arr.length; i++) {
    if (arr[i] > max) {
      max2 = max;
      max = arr[i];
    }
  }
  console.log(max2);
}
