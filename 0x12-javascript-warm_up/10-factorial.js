#!/usr/bin/node
// Script that computes and prints a factorial.
function factorial (Value, Step) {
  if (Step === 1) return Value;
  Value = factorial(Value * (Step - 1), Step - 1);
  return Value;
}

let num = parseInt(process.argv[2]);
if (isNaN(num)) {
  num = 1;
}
console.log(factorial(num, num));
