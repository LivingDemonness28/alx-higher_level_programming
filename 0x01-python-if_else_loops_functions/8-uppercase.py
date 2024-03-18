#!/usr/bin/python3
def uppercase(s):
  for char in s:
    if ord('a') <= ord(char) <= ord('z'):
      uc_char = chr(ord(char) - (ord('a') - ord('A')))
      print(uc_char, end='')
    else:
      print(char, end='')
  print()
