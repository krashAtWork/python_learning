
#sets

#sets store only unique values
# they are fast because they use hashing
# sets are unordered
# you can do union, intersection on sets

#{}

"""x = {2, 3, 2, 3}
y = set()
z =[ 'a','b', 'a']
z = set(z)

print(x,"\n", y, "\n", z, "\n")i
"""

# add
# remove
# length
#check memebership
# pop
# del

# pop
x = {1, 2, 3, 4}
x.pop()
print(x)

# set operations

## Dictionaries
# key/value pairs
# unordered

#creating dictionaries
mydict ={ 'flower of evil' : 10, 'healer' : 9.5, 'my girlfriend is a gumiho' : 9}
print(mydict)
print(mydict['flower of evil'])

# add or update
# delete
print(mydict.keys())
print(mydict.items())
print(mydict.values())

for key in mydict:
    print(key, mydict[key]);

# list comprehension
    
