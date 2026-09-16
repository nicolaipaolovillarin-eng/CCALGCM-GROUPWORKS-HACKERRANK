#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagram(s):
    # Write your code here
    half = ((len(s))//2)
    if (len(s) % 2) != 0:
        return -1
    else:
        string1 = sorted(s[:half])
        string2 = sorted(s[half:])
        currentindex1 = 0
        currentindex2 = 0
        count = 0
        while currentindex1 < half and currentindex2 < half:
            if (string1[currentindex1] == string2[currentindex2]):
                count += 1
                currentindex1 += 1
                currentindex2 += 1
            elif (string1[currentindex1] < string2[currentindex2]):
                currentindex1 += 1
            else:
                currentindex2 += 1
        return half - count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
