#!/usr/bin/node
const string = process.argv[2];
const number = parseInt(string);

if (isNaN(number)) {
  console.log('Missing number of occurences');
} else {
  for (let i = 1; 0 < i <= number; i++) {
    console.log('C is fun');
  }
}
