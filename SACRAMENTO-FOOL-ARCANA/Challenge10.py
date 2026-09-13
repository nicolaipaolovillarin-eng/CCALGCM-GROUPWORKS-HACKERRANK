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
    if len(s) % 2 == 1 :
        return -1
    else :
        changes = 0
        i = 0    
        while i < 26 :
            changes += abs(s[:len(s) // 2].count(chr(i + 97)) - s[len(s) // 2:].count(chr(i + 97)))
            i += 1
        
        return changes // 2
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
