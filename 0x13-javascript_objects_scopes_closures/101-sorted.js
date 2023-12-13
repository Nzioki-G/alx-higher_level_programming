#!/usr/bin/node
const dict = require('./101-data.js').dict;

const newDict = {};
let key, val;
for ([key, val] of Object.entries(dict)) {
  if (val in newDict) {
    newDict[val].push(key);
  } else {
    newDict[val] = [key];
  }
}

console.log(newDict);
