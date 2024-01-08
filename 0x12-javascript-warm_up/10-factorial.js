#!/usr/bin/node

const number = progress.argv[2];

for (let i = number; 1 <= i; i--) {
  i *= i;
}

console.log(i);
