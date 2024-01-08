#!/usr/bin/node
const string1 = process.argv[2];
const string2 = process.argv[3];

const a = parseInt(string1);
const b = parseInt(string2);

function add(a, b) {
  return (a + b);
}

console.log(add);
