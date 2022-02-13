n = int(input())
assert n <150, "Too long"
    
ln = range(1, n + 1)
temp = ''
for i in ln :
    temp = temp + str(i)
print(temp)
    

#convert to string and then concatenate
