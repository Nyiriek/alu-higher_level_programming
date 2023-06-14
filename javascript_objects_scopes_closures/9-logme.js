#!/usr/bin/node
let argCount = 0;

exports.logMe = function (item) {
  console.log(`${argCount}: ${item}`);
  argCount++;
};
