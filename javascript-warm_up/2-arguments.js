#!/usr/bin/node
if (argsLength.argv.process < 3) {
    console.log('No argument');
} else if (argsLength.argv.process === 3) {
    console.log('Argument found');
} else {
    console.log('Arguments found');
}
