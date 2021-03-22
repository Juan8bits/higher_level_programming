#!/usr/bin/node
// Script that prints the addition of 2 integers.
function add (number1, number2) {
  return parseInt(number1) + parseInt(number2);
}

console.log(add(process.argv[2], process.argv[3]));
