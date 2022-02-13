#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    # find uniques in the array
    uniques = []
    for i in ar:
        if i not in uniques:
            uniques.append(i)
    # print(uniques)
    # for each unique find the cont
    maps = {}
    for i in uniques:
        count = 0 
        for j in ar:
            if(j == i):
                count = count+1
        maps[i] = count
    # print(maps)

    # if count is a multiple of 2 : 3/ 2 = 1, 3%2 = 1 1/2 = 0 1%2 = 1
    pairs = 0
    for key, value in maps.items():
        rem = value % 2
        quo  = int(value / 2)
        if(rem == 0):
            pairs = pairs + quo
        else:
            if(quo > 0):
                # print("quo =" ,  quo)
                pairs = pairs + quo
            
    # print(pairs)
    return pairs
        
            



n = int(input().strip())

ar = list(map(int, input().rstrip().split()))

result = sockMerchant(n, ar)


