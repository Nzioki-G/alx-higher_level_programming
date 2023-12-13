#!/usr/bin/node
// prints <no. of args already printed>: <arg>
let count = 0;
exports.logMe = function (item) {
  console.log(count + ': ' + item);
  count++;
};
