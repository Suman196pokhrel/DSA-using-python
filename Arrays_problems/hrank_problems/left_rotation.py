#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the 'rotateLeft' function below.

# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr


def rotateLeft(d, arr):

     # Write your code here
     for i in range(d):
          arr.append(arr.pop(0))
     return arr

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = rotateLeft(d, arr)
    print(result)


