#!/usr/bin/node
let string = process.argv[2];
let number = parseInt(string);
if (isNaN(number)) {
  console.log('Not a number');
} else {
  let string1 = number.toString();
  console.log('My number: ' + string1);
}
