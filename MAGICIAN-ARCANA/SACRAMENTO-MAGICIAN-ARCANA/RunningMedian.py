#!/bin/python3

import math
import os
import random
import re
import sys
import bisect

#
# Complete the 'runningMedian' function below.
#
# The function is expected to return a DOUBLE_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#

def runningMedian(a):
    # Write your code here
    median:float = []
    runningList = [] 
    
    for i in range(len(a)) :
        
        index = bisect.bisect(runningList,a[i])
        runningList.insert(index, a[i])
        length = i + 1
        
        if (length) % 2 == 0:
            temp = (runningList[length//2] + runningList[length//2 - 1]) / 2
            median.append(float(temp))
        else:
            median.append(float(runningList[length // 2]))
    
    return median

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input().strip())

    a = []

    for _ in range(a_count):
        a_item = int(input().strip())
        a.append(a_item)

    result = runningMedian(a)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
