

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # Write your code here
    arr_sum = []
    for i in range(1,5):
         for j in range(1,5):
              arr_sum.append(arr[i-1][j-1]+arr[i-1][j]+arr[i-1][j+1] 
                            + arr[i][j]
                            + arr[i+1][j-1]+arr[i+1][j]+arr[i+1][j+1])
     
    return max(arr_sum)
    

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)
    print(result)
