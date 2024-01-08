#!/usr/bin/node
const number = process.argv[2];
const n = parseInt(number);

function fact (n) {
  if (n === undefined || isNaN(n)) {
    return (1);
  } else if (n <= 1) {
    return (1);
  } else {
    return (n * fact(n - 1));
  }
}

console.log(fact(n));
