#!/usr/bin/node
const numberOfArguments = process.argv.length;
if (numberOfArguments < 3) {
  console.log('No argument');
} else if (numberOfArguments === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found')
}
