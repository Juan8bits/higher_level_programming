#!/usr/bin/node
/* Function that prints the number of arguments already printed
   and the new argument value. (see example below).
*/
let times = 0;
exports.logMe = function (item) {
  console.log(times + ': ' + item);
  times++;
};
