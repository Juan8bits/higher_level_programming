#!/usr/bin/node
/*
    Class Square that defines a square and inherits from Square of 5-square.js.

    -You must use the class notation for defining your class and extends.
    -Create an instance method called charPrint(c) that prints the rectangle using the character c.
    -If c is undefined, use the character X.
*/
const SquareHin = require('./5-square');
module.exports = class Square extends SquareHin {
  charPrint (c) {
    if (typeof c === 'undefined') { c = 'X'; }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.height));
    }
  }
};
