#!/usr/bin/node
let firstArgument = process.argv[2];
if (firstArgument === undefined) {
    console.log('No argument');
} else {
    console.log(process.argv[2]);
}
