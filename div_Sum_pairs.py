#div_sum_pairs

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisibleSumPairs(n, k, ar):
    # Write your code here
    # print(n, k)
    # print(ar)
    count = 0
    for i in range(0,n):
        # print(ar[i])
        for j in range(i+1, n):
            # print(ar[j])
            if((ar[i]+ ar[j]) % k):
                count = count + 1
    print(count)
    return count

            

   

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

k = int(first_multiple_input[1])

ar = list(map(int, input().rstrip().split()))

result = divisibleSumPairs(n, k, ar)

   
