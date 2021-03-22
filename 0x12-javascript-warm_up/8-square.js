#!/usr/bin/node
// Script that prints a square.
if (process.argv[2] && !isNaN(process.argv[2])) {
  const size = parseInt(process.argv[2]);
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
} else {
  console.log('Missing size');
}
