#!/usr/bin/node
/*
   Class Rectangle that defines a rectangle.

    -You must use the class notation for defining your class.
    -The constructor must take 2 arguments w and h.
    -Initialize the instance attribute width with the value of w.
    -Initialize the instance attribute height with the value of h.
    -If w or h is equal to 0 or not a positive integer, create an empty object.
    -Create an instance method called print() that prints the rectangle using the character X.
*/
module.exports = class Rectangle {
  constructor (w, h) {
    if ((Number.isInteger(w) && w > 0) && (Number.isInteger(h) && h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let h = 0; h < this.height; h++) {
      console.log('X'.repeat(this.width));
    }
  }
};
