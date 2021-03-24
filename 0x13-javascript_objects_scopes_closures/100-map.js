#!/usr/bin/node
// Script that imports an array and computes a new array.
const list = require('./100-data').list;
let newArr = []; let i = 0;
console.log(list);
newArr = list.map(val => val * i++);
console.log(newArr);
