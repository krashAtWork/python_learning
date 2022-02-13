# migratory birds

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def migratoryBirds2(arr):
    uniques = []
    for i in range(0, len(arr)):
        if(arr[i] not in uniques):
            uniques.append(arr[i])
    print(uniques)

    maps= {}
    for i in uniques:
        count = 0
        for j in arr:
            if(i == j):
                count = count + 1
        maps[i] = count
    print(maps)

    #list values of a dictionary.
    print(max(maps.values()))
    max_occ = max(maps.values())

    for key, value in maps.items():
        if(value  == max_occ):
            result = key
    print(result)

    return result

    


def migratoryBirds(arr):
    # Write your code here
    # max = arr[0]
    uniques= []
    idx_count = []
    # a map is needed
    for i in range(0, len(arr)):
        if(arr[i] not in uniques):
            uniques.append(arr[i])
    #print(uniques)

    maps={}
    for i in uniques:
        count = 0
        for j in arr:
            if(i == j):
                count = count + 1
        maps[i] = count
    print(maps)

    for i in uniques:
        count = 0
        for j in arr:
            if(i == j):
                count = count + 1
        # idx_count.append(i)
        idx_count.append(count)

    print(idx_count)

    max =  idx_count[0]
    idx = 0
    for i in range(1 ,len(idx_count)):
        if(idx_count[i] > max):
            max = idx_count[i]
            idx = i
    print(idx)
            

       
    
    print(uniques[idx])

    return uniques[idx]
        
            







        

        # if(arr[i] > max):
        #     max = arr[i]
        #     idx = i

    
    # print(idx)
    # return idx



arr_count = int(input().strip())

arr = list(map(int, input().rstrip().split()))

result = migratoryBirds2(arr)

  
