#!/usr/bin/node
// Script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.
const Dict = require('./101-data').dict;
const mydict = {};
for (const key in Dict) {
  // unknow behavior with ' in undefined
  if (mydict[Dict[key]] === undefined) {
    mydict[Dict[key]] = [key];
  } else {
    mydict[Dict[key]].push(key);
  }
}
console.log(mydict);
