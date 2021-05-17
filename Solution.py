#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def solve(a, b):
    b = b % ((10**9 + 7) - 1)
    return pow(a,b,10**9 + 7)
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input().strip())

    for t_itr in xrange(t):
        first_multiple_input = raw_input().rstrip().split()

        a = first_multiple_input[0]

        b = first_multiple_input[1]

        result = solve(int(a), int(b))

        fptr.write(str(result) + '\n')

    fptr.close()
