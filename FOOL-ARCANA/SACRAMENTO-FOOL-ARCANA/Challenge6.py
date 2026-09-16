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
    min:int = 0
    max:int = 0
    arr.sort()
    
    min = sum(arr) - arr[4]
    max = sum(arr) - arr [0]
    
    print(f"{min} {max}")
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
