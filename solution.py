#def rotate(n, lst):
    ## 3, 2, 1
    ## 1 : 1, 3, 2
    ## 2 : 2, 1, 3
    ## 3 : 3, 2, 1
    ## rotating once  means
    
    #for j in range(0,n):
    #    #for i in range(0, len(lst)):
    #    #print(lst[i])
    #    #temp = lst[i]
    #    #nwlst[i] = lst[len(lst) - 1-i]
    #    #lst[0] = lst[2]
    #    #lst[1] = lst[0]
    #    #lst[2] = lst[1]
    #        if( i == 0 ) :
    #            nwlst = []
    #            nwlst.append( lst[len(lst) -1 ])
    #        else:
    #            nwlst.append( lst[i-1])
    #         lst = nwlst.copy()
    #return lst


def rotate2(k, lst):
   for j in range(0, k ):
      for i in range(0, len(lst) ):
         cur = lst[i]
         if(i == 0):
            lst[i] = lst[len(lst) -1]
         else:
            lst[i] = prev
         prev = cur
   return lst
    #for j in range(0, n):
        
           







n = 3
lst = [3, 2, 1, 4]
result =  rotate2(n , lst)
print(result)


