#!/usr/bin/node
const argument = process.argv.length - 2;
if (argument === 0) {
  console.log('No argument');
} else {
  console.log(argument[2]);
}
