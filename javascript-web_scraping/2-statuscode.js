#!/usr/bin/node
const request = require('request');

request(process.argv[2], (err, res) => {
  if (err) {
    console.log(err);
  }
  console.log('code: ', res && res.statusCode);
});
