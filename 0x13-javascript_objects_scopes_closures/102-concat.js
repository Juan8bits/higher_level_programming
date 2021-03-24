#!/usr/bin/node
// Script that concats 2 files.
const fs = require('fs');
const file1 = fs.readFileSync(process.argv[2], 'utf8');
const file2 = fs.readFileSync(process.argv[3], 'utf8');
fs.appendFileSync(process.argv[4], file1 + file2, 'utf8');
