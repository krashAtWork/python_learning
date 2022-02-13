# s1= input("No of pens ")
# s1 = int(s1)
# s2 = input ("No of pencils ")
# s2= int(s2)
# print (s1,s2)

# i1 = input("unit cost of pen ")
# i1 = int(i1)
# i2 = input("unit cost of pencils ")
# i2 = int(i2)
# print(i1,i2)

# total_cost = s1*i1  +  s2*i2

# print(total_cost)

flinput = input("Enter no of pens , pencils and unit cost of them respectively, giving a space in between")
print(flinput)
# separate the strings based on 
flinput2 = flinput.split(" ")
# print(flinput2)
n_pens = int(flinput2[0])
assert n_pens > 1, 'input is not correct'
n_pencils =  int(flinput2[1])
uc_pens =  int(flinput2[2])
uc_pencils = int(flinput2[3])
print(n_pens * uc_pens + n_pencils * uc_pencils )

# how to take an input string and split it using a space in between
# flinput.split(" ")
# how do you assert in python that the input is in a certain range
# assert n_pens > 1, 'input is not correct'


