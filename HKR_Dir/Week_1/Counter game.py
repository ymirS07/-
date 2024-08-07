#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'counterGame' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#

def counterGame(n):
    # Write your code here
    count = 0
    if n == 1:
        return 'Louise'
    while 1 < n:
        log_2 = math.log2(n)
        if log_2 % 1 == 0:
            n /= 2
        else:
            n -= 2 ** int(log_2)
        count += 1
    if count % 2 == 0:
        return 'Richard'
    else:
        return 'Louise'
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = counterGame(n)

        fptr.write(result + '\n')

    fptr.close()
