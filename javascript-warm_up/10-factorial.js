#!/usr/bin/node
function factorial (m) {
  if (isNaN(m)) {
    return 1;
  } else if (m === 0) {
    return 1;
  } else {
    return factorial(m - 1) * m;
  }
}

const number = parseInt(process.argv[2]);
console.log(factorial(number));
