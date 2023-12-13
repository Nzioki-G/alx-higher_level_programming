#!/usr/bin/node
// using Array.map() to iterate
const list = require('./100-data').list;
/*
let newList = [];
for (let i = 0; i < list.length; i++) {
  newList[i] = i * list[i];
}
*/
const nList = list.map((element, index) => { return element * index; });
console.log(list);
console.log(nList);
