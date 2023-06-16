#!/usr/bin/node
const request = require('request');

request(process.argv[2], (err, res, body) => {
  if (err) {
    console.log(err);
  }

  const filteredFilms = JSON.parse(body).results.filter((film) => {
    return film.characters.filter((url) => { return url.includes('/18/'); }).length;
  }).length;
  console.log(filteredFilms);
});
