#!/usr/bin/node
function factorial (num) {
  if (num == 0 || num == 1 || isNaN(num)) {
    return (1);
  }
  fact = num * factorial(num - 1);

  return (fact);
}
console.log(factorial(parseInt(process.argv[2])));
