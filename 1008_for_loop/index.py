"""
for loop:definite number of iterations are known, used to traverse through the iterables 
inbuilt class  = range(start, end, step ) create the range of numbers
return the range object address

to extract the value in the object 
1. typecasting to list 
2. for loop

Syntax :

for ref_var in iterables:
    statement
"""

#print "Hello World" in 5 times


for x in range(5):
    print("Hello World")

print()

start = 0

for x in range(0,5):
    print("Hello World")


# print the number from 1 to 10

for num in range(1, 11):
    print(num)

# Its skip the last number

# print the number from 10 to 1

for num in range(10, 0, -1):
    print(num, end=" ")

print()
# print number -1 to -10 

for num in range(-1 , -11, -1):
    print(num, end=", ")

