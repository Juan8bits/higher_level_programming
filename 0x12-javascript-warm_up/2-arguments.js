#!/usr/bin/node
// Script that prints a message depending of the number of arguments passed.
if (process.argv[2]) {
  if (process.argv[3]) {
    console.log('Arguments found');
  } else {
    console.log('Argument found');
  }
} else {
  console.log('No argument');
}
