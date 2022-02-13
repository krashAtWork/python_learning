# strings
x = "frog"
print(x[1])# index is []

# lists
x = ["Healer", "Gumiho", "Flower"]
print(x[2])

# tuples
x = ("master", "tomorrow with you","our secret")
print(x[2])

# slicing
x = "Flower of evil"
print( x[ 0 : 6] )
print( x[ 6 : ] )
print( x[-1 : ] )
print( x[-4 : ] )
print( x[  : -1])

# concatenating
x = "My girlfriend is a "
y = "Gumiho"
print(x + y)


str1 = ["Healer", "Gumiho", "Flower"]
str2 = ["Reply 1988", "my youth"]
print(str1+ str2)


tup1 = ("master", "tomorrow with you","our secret")
tup2 = ("hometown cha",)
print(tup1 + tup2)

# multiplying
tup_mul = tup2 * 3
print(tup_mul)


# check presence

print( "hometown" in tup_mul)
print("Healer" in str1)
print("Gumiho" in str2)

#iterating
for item in tup1:
    print(item)

for index, item in enumerate(str1):
    print(index, item)

# count of items
cnt = [1, 2, 3, 8, 7,5, 6,7 ];
print(len(cnt))

#min max sum

# sorting always returns as a list

print(sorted(tup1))
print(sorted(cnt))

# count
print(tup_mul.count("hometown cha"))
print( str1.count("Gumiho"))

# index
print(tup_mul.index('hometown cha'))

# unpacking
x, y, z = tup1
print(x, y, z)

















