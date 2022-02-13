#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def superReducedString2(s): #aa
    changed = True
    while changed and s != "":#  do until s != "" and there has been a change in thestring, because we have to do onlyafter that
        changed = False
        for i in range(len(s) - 1):
            if s[i] == s[i+1]:
                changed = True
                s = s[:(i)] + s[(i+2):] #if there is a match, save everything before and after
                break

    if s == "":
        print('Empty String')
    else:
        print(s)
            






def superReducedString(s):
    # Write your code here
    # detect two adjacent character which are same
    lst_s = list(s)
    idx = []
    for i in range(1, len(lst_s) - 1):
        print( lst_s[i], lst_s[i+1])
        if(lst_s[i] == lst_s[i+1] ):
            lst_s.remove(lst_s[i])
            lst_s.remove(lst_s[i+1])

    print(idx)
    replaced = ""
    for i in range(0, len(lst_s) ):
        if i not in idx:
            replaced =  replaced + lst_s[i]
    print(replaced)
    

        



    return "abc"

    
    
    



    

s = input()

result = superReducedString2(s)


    
