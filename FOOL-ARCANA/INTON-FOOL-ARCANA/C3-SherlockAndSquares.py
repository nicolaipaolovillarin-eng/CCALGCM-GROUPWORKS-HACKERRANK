#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'squares' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#

def squares(a, b):
    # Write your code here
    lowestfound = highestfound = 0
    a-=1 #offset by -1 so that the first loop starts back to normal
    while lowestfound != 1:
        a+=1
        lowestfound = bool(math.sqrt(a) == int(math.sqrt(a)))

    b+=1 #offset by 1 so that the first loop starts back to normal
    while highestfound != 1:
        b-=1
        highestfound = bool(math.sqrt(b) == int(math.sqrt(b)))
    return int((math.sqrt(b) - math.sqrt(a)) + 1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
