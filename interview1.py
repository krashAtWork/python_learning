input = "abcbab"


print(set(list(input)))
ch = set(list(input))#a, b, c
# first find words that are reproduce
count= 0
for i in ch: #a #b #c
    #for j in input:
        count = 0
        for j in range(0, len(input)):#a b c b
            if (i == input[j]):
                count = count +1 #1 2 #1 2 3
        if(count >1):
            print(i, count)# a 2  #b 3 

    


