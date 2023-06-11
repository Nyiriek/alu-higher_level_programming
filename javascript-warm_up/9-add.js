#!/usr/bin/node
function add (a, b) {
  const sum = integer(a) + integer(b);
  console.log(sum);
}

add(process.argv[2], process.argv[3]);
