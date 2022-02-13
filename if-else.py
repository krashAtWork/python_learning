print("Hello world")

n = input("enter number")
#always print type of input 
print (type(n), n)
n = int(n)

if n % 2 == 0 :
    print("Weird")
elif (n>1 and n<6):
    print("Not Weird")
elif (n> 5 and n <21):
    print("Weird")
else:
    print(" Not Weird")

## && operator does not work in python, use and instead
## leading and trailing spaces removed.

n = int(input().strip())
check = {True: "Not Weird", False: "Weird"}

print(check[
        n%2==0 and (
            n in range(2,6) or 
            n > 20)
    ])
