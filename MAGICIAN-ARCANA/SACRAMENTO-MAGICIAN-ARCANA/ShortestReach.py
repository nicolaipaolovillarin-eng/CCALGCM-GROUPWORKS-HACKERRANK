#!/bin/python3

import math
import os
import random
import re
import sys
import queue

#
# Complete the 'bfs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. 2D_INTEGER_ARRAY edges
#  4. INTEGER s
#

def bfs(n, m, edges, s):
    # Write your code here
    frontier = queue.Queue()
    isVisited = [False] * n
    distances = [-1] * n
    
    frontier.put(s)
    isVisited[s - 1] = True
    distances[s - 1] = 0
    
    while not frontier.empty():
        i = frontier.get()
        
        
        for x in range(len(edges)):
            if edges[x][0] == i and isVisited[edges[x][1]-1] is False:
                frontier.put(edges[x][1])
                isVisited[edges[x][1]-1] = True
                distances[edges[x][1]-1] = distances[i-1] + 6
            elif edges[x][1] == i and isVisited[edges[x][0]-1] is False:
                frontier.put(edges[x][0])
                isVisited[edges[x][0]-1]  = True
                distances[edges[x][0]-1] = distances[i-1] + 6

    distances.pop(s-1)
    
    return distances
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
