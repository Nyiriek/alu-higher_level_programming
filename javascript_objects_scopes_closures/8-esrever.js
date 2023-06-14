#!/usr/bin/node
exports.esrever = function (list) {
  const reversedList = [];
  for (let j = list.length - 1; j >= 0; j--) {
    reversedList.push(list[j]);
  }
  return reversedList;
};
