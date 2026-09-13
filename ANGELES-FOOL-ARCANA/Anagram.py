#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagram(s):
    if len(s) % 2 != 0:
        return -1

    a = s[:len(s)//2]
    b = s[len(s)//2:]

    count_a = Counter(a)
    count_b = Counter(b)

    changes = 0

    for c in count_a:
        if count_a[c] > count_b[c]:
            changes += count_a[c] - count_b[c]

    return changes

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
