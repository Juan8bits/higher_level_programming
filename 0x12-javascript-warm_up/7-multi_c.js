#!/usr/bin/node
// Script that prints x times C is fun.
if (process.argv[2]) {
  for (let i = 1; i <= parseInt(process.argv[2]); i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
