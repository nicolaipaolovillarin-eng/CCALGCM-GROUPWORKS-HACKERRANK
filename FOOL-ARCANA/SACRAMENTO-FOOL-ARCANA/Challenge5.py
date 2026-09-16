#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def minimumDistances(a,n):
    # Write your code here
    min:int = -1
    
    i = 0
    while i < n - 1: 
        j = i + 1
        while j < n:
            if a[i] == a[j]:
                if min != -1:
                    if min > j-i:
                        min = j-i
                else:
                    min = j-i
            j += 1
        i += 1
    return min             

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a,n)

    fptr.write(str(result) + '\n')

    fptr.close()
