#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let j = 0; j < this.height; j++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const x = this.width;
    this.width = this.height;
    this.width = x;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
