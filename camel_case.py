#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'camelcase' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
# 

def camelcase(s):
    # Write your code here
    count_of_words = 1
    for i in s:
        if(i.isupper()):
            count_of_words = count_of_words+ 1
    return count_of_words


   

s = input()

result = camelcase(s)
print(result)

   
