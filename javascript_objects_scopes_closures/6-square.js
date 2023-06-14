#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (c) {
    const char = c || 'X';

    for (let m = 0; m < this.height; m++) {
	    console.log(char.repeat(this.width));
    }
  }
}

module.exports = Square;
