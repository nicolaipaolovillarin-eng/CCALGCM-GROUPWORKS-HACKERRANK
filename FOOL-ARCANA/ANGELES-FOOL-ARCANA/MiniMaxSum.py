#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    total = sum(arr)
    sums = [total - x for x in arr]
    print(min(sums), max(sums))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
