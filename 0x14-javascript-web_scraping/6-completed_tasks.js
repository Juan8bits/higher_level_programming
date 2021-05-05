#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const myObj = {};

request.get(url, function (err, response, body) {
  if (err) {
    console.error(err);
  } else {
    const jsonResponse = JSON.parse(body);
    for (let i = 0; jsonResponse[i]; i++) {
      if (jsonResponse[i].completed === true) {
        if (jsonResponse[i].userId in myObj) {
          myObj[jsonResponse[i].userId] += 1;
        } else {
          myObj[jsonResponse[i].userId] = 1;
        }
      }
    }
  }
  console.log(myObj);
});
