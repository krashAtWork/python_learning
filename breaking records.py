## breaking records

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    min = scores[0]
    max = scores[0]
    change_min = 0
    change_max = 0
    for i in range(1, len(scores) 9):
        if(scores[i] < min):           
            min = scores[i]
            print(min)
            change_min = change_min + 1


        if(scores[i] > max):
            max = scores[i]
            change_max = change_max + 1
    # print(change_min , change_max)
    return [change_min , change_max]

    # Write your code here



n = int(input().strip())

scores = list(map(int, input().rstrip().split()))

result = breakingRecords(scores)


