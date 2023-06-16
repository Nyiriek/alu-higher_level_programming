#!/usr/bin/node
const { argv } = require('process');
const request = require('request');
const fs = require('fs');

const url = argv[2];
const filePath = argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }

  fs.writeFileSync(filePath, body);
});
