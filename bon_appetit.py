#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#

def bonAppetit(bill, k, b):
    # Write your code here
    # remove kth item from bill:
    sum = 0
    for i in range(0, len(bill)):
        if(i != k):
            print(bill[i])
            sum  = sum  + bill[i]
    aac = sum/2

    if(aac ==  b):
        print("Bon Appetit")
    else:
        payback = b - aac
        print(int(payback))


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
