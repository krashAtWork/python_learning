#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    print(s)
    hr = ""
    mn = ""
    sc = ""
    ap = ""
    # How to divide a string by :
    # first find all indexes where : this is available
    # 07:05:45 PM
    end = [2, 5, 8]
    for i in range(0, end[0]):
        hr += str(s[i])
    for j in range(end[0] + 1, end[1]):
        mn += str(s[j])
    for k in range(end[1] + 1, end[2]):
        sc += str(s[k])
    for m in range(8,10):
        ap += s[m]
    
    print(hr, mn, sc, ap)
    # lst = []
    # lst.append[hr, mn, sc, ap]
    # lst_int = []
    # for i in lst:
    #     temp = int(i)
    #     lst_int.append()

    if(ap == "PM"):
        hr = int(hr) + 12
    elif (ap == "AM" and "12" == hr):
        hr = "00"
    else:
        hr = int(hr)

    time_convtd = str(hr) + ":" + str(mn) + ":" + str(sc)

    return time_convtd
    
    

    
   # return "abc"


   
s = input()

result = timeConversion(s)
print(result)

