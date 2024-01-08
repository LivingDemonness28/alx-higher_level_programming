#!/usr/bin/node
const number = process.argv[2];
let i = number;

for (i; 1 < i; i--) {
  i *= i;
}

console.log(i);
