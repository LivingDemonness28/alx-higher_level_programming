#!/usr/bin/node
const number = process.argv[2];
const n = parseInt(number);

function fact (n) {
  if (number === undefined) {
    console.log(1);
  } else if (isNaN(n)) {
    console.log(1);
  } else {
    return (n * fact(n - 1));
  }
}
