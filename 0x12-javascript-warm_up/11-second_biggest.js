#!/usr/bin/node
// Script that searches the second biggest integer in the list of arguments.
const arr = process.argv.slice(2);
if (arr.length <= 1) {
  console.log('0');
} else {
  arr.sort(function (a, b) { return b - a; });
  console.log(parseInt(arr[1]));
}
