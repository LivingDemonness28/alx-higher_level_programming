#!/usr/bin/node

const number = process.argv[2];

for (let i = number; 1 <= i; i--) {
  i *= i;
}

console.log(i);
