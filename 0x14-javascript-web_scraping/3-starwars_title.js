#!/usr/bin/node
const request = require('request');
const id = process.argv[2];

const url = 'https://swapi-api.hbtn.io/api/films/' + id;

request.get(url, function (err, response, body) { /* Aparently it needs all args */
  if (err) {
    console.error(err);
  } else {
    console.log(JSON.parse(body).title); /* Converts to JS object */
  }
}
);
