#!/usr/bin/node
const string = process.argv[2];
const number = parseInt(string);

if (isNaN(number)) {
  console.log('Missing size');
} else {
  let string1 = 'X';

  for (let i = 1; i < number; i++) {
    string1 += 'X';
  }

  for (let j = 0; j < number; j++) {
    console.log(string1);
  }
}


