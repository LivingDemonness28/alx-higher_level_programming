#!/usr/bin/node
const string = process.argv[2];
const number = parseInt(string);
if (isNaN(number)) {
  console.log('Not a number');
} else {
  const string1 = number.toString();
  console.log('My number: ' + string1);
}
