#!/usr/bin/node
// Script that computes and prints a factorial.
function factorial (Step) {
  if (Step === 1) return Step;
  Step = Step * factorial(Step - 1);
  return Step;
}

let num = parseInt(process.argv[2]);
if (isNaN(num) || num === 0) {
  num = 1;
}
console.log(factorial(num));
