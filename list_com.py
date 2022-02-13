x = int(input())
y = int(input())
z = int(input())
n = int(input())

sol = []

rangeX = range(0, x+1) 
rangeY = range(0, y+1) 
rangeZ = range(0, z+1) 

for i in rangeX:
    for j in rangeY:
        for k in rangeZ:
            if (i + j + k) != n:
                temp = [i, j, k]
                sol.append(temp)
            
# how to add to a list in python - .append()

print(sol)