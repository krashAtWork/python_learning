#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    # Write your code here
    #  1 - step1
    #  2 - step2
    #  if (step 1 == step 2) just break  --> yes or no
    step1 = x1
    step2 = x2
    res = "NO"
    overran = "NO"
    while(step1 != step2):
        step1 = step1 + v1
        step2 = step2 + v2
        if(step1 > 10000 or step2 >10000):
            res = "NO"
            overran = "YES"
            break
    res = "YES"
    if(res == "YES" and overran == "YES"):
        res = "NO"
    return res



first_multiple_input = input().rstrip().split()

x1 = int(first_multiple_input[0])

v1 = int(first_multiple_input[1])

x2 = int(first_multiple_input[2])

v2 = int(first_multiple_input[3])

result = kangaroo(x1, v1, x2, v2)

print(result)