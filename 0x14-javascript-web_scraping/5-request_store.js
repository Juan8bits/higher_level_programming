#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const file = process.argv[3];

request(url, function (error, response) {
  if (error) {
    return console.error(error);
  }
  fs.writeFile(file, response.body, function (err) {
    if (err) {
      return console.error(err);
    }
  }
  );
}
);
