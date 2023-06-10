#!/usr/bin/node

const argsLength = process.args.length -2;

if (argsLength < 3) {
    console.log('No argument');
} else if (argsLength === 3) {
    console.log('Argument found');
} else {
    console.log('Arguments found');
}
