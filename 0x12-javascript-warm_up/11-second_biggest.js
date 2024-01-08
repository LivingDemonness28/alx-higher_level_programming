#!/usr/bin/node
const arr1 = process.argv.slices(2);

function second_biggest (arr1) {
  len1 = arr1.length
  if (arr1 === undefined) {
    return (0);
  } else if (len1 === 1) {
    return (0);
  } else {
    while (true) {
      let swapped = false;

      for (let i = 0; i < len1 - 1; i++) {
        if (arr1[i] > arr1[i + 1]) {
          [arr1[i], arr1[i + 1]] = [arr1[i + 1], arr1[i]];
          swapped = true;
        }
      }

      if (!swapped) {
        break;
      }
    }
    return (arr1[len1 - 2]);
  }
}

console.log(second_biggest(arr1));
