#!/usr/bin/node
const number = process.argv[2];
const n = parseInt(number);

function fact (n) {
  if (n === undefined || isNaN(n)) {
    console.log(1);
  } else {
    return (n * fact(n - 1));
  }
}

fact(n);
