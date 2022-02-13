#!/bin/python3

from itertools import count
import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
      spec_char = "!@#$%^&*()-+"
      for cchar in password:
        countUpper = 0
        #print(cchar)
        if(cchar.isalpha()):
            if(cchar.isupper()):
                countUpper = countUpper + 1  
                break     


      for cchar in password:
        countLower = 0
        if(cchar.isalpha()):
            if(cchar.islower()):
                countLower = countLower + 1
                break

      for cchar in password:
        countSpecChar = 0
        if(cchar in list(spec_char)):
            countSpecChar = countSpecChar + 1
            break

      for cchar in password:
        countNum = 0
        if(cchar.isnumeric()):
            countNum  = countNum + 1
            break

    # there should be atleast
      present = countUpper + countLower + countNum + countSpecChar #1
      to_add = 4 - present #3
      if(n < 6):# violating minimum
            if(to_add >= 6-n):
                return to_add
            else: 
                return 6-n
      else:
        return to_add












    # Return the minimum number of characters to make the password strong
        """
    Its length is at least 6
    It contains at least one digit.
    It contains at least one lowercase English character.
    It contains at least one uppercase English character.
    It contains at least one special character. The special characters are: !@#$%^&*()-+ 
            """

    ## the perfect password
  
    
    # detect all the cases
    
    
    

            
        






n = int(input().strip())

password = input()

answer = minimumNumber(n, password)

print(answer)

    