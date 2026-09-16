#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    arr = sorted(arr)
    minsum = maxsum = 0
    for index in arr[0:4]:
        minsum += index
    for index in arr[1:]:
        maxsum += index
    print(minsum, maxsum)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
