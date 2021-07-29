#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#
# This method did not execute within the time limit
# def arrayManipulation(n, queries):
#     # Write your code here
#     arr = [0 for i in range(n+1)]
#     for q in queries:
#         for j in range(q[0],q[1]+1):
#             arr[j] = arr[j]+q[2]
     # return max(arr)

def arrayManipulation(n, queries):
    # Write your code here
    arr = [0 for i in range(n+2)]
    # Prefix-Sum Algorithm 
    for quer in queries:
        a = quer[0]
        b = quer[1]
        k = quer[2]
        arr[a-1] = arr[a-1] + k
        arr[b]= arr[b] + (-k)
    
    # simple Max Val Calculation 
    maxval = 0
    val = 0
    for elem in arr:
        val = val + elem
        if val > maxval:
            maxval = val
    return maxval
    

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    print(result)
