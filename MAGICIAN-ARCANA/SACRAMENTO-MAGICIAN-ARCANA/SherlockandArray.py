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
    result = "NO"
    low = 0
    high = len(arr) - 1
    
    while high >= low and result == "NO":
        mid = (high + low) // 2
        
        if sum(arr[:mid]) == sum(arr[mid + 1:]) :
            result = "YES"
        
        elif sum(arr[:mid]) > sum(arr[mid + 1:]) :
            high = mid - 1
            
        elif sum(arr[:mid]) < sum(arr[mid + 1:]) :
            low = mid + 1
            
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()
