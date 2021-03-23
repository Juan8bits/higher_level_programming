#!/usr/bin/node
// Function that returns the reversed version of a list.
exports.esrever = function (list) {
  const RevCopy = new Array(list.length);
  for (let i = list.length - 1; i >= 0; i--) { RevCopy.push(list[i]); }
  return RevCopy;
};
