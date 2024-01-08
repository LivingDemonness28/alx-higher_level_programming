#!/usr/bin/node
const number = process.argv[2];
let i = number;

for (i; 0 < i; i--) {
  i *= i;
}

console.log(i);
