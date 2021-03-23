#!/usr/bin/node
// Function that returns the number of occurrences in a list.
exports.nbOccurences = function (list, searchElement) {
  let occurrences = 0; let i = 0;
  while (list[i]) {
    if (searchElement === list[i]) {
      occurrences++;
    }
    i++;
  }
  return occurrences;
};
