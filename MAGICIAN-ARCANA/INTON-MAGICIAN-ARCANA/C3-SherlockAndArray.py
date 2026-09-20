#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'balancedSums' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def balancedSums(arr):
    # Write your code here
    found = "NO"
    leftSide = 0
    totalNumber = sum(arr)
    arrayIndex = 0
    while found != "YES" and arrayIndex < len(arr):
        if (leftSide) == (totalNumber - (arr[arrayIndex])) / 2:
            found = "YES"
        else:
            leftSide += arr[arrayIndex]
            arrayIndex += 1
    return found

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()
