#!/usr/bin/node
const args = process.argv.slice(2);
const integers = args.map(arg => parseInt(arg));

if (integers.length < 2) {
  console.log(0);
} else {
  const sortedIntegers = integers.sort((a, b) => b - a);
  console.log(sortedIntegers[1]);
}
