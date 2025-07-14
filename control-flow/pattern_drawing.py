#!/usr/bin/env python3
# Drawing patterns with loops
length = int(input("Enter the size of the pattern:"))
i = 1
while i <= length:
    i += 1
    for _ in range(length):
      print("*", end='')
    print()
     
  
