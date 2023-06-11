#!/usr/bin/node
function add (a, b) {
  const sum = parseInt(a) + parseInt(b);
  console.log(sum);
}

add(process.argv[2], process.argv[3]);
