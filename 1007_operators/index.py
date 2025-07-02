# Operators are used to perform operations on operands

# 1. Arithmetic Operators :  (+ , - ,  * ,  / ,  % ,  //(floor division) , **(power/exponent))
# 2. Relational Operators / Comparison Operators : < , > , >= , <= , == , !=
# 3. Logical Operators   : and , or , not
# 4. Bitwise Operators   : & , | , !
# 5. Assignment Operators : ==
# 6. Identity Operators
# 7. Membership Operators


# Perform Arithmetic Operators

# Relational Operators / Comparison Operators

a = 10
b = 20

print( a > b)
print(a < b)
print(a == b)


############################################################################################
# ASCII value

# a - z     a = 97  z = 122
# A - Z     A = 65   Z = 90

print("a" > "c")      #97 > 99
print("c" > "a")

print("ac" > "ab")  
print(9799 > 9798)

print(10 != 20)          # True
print(10 != 10)          # False

# ord(char) == ASCII value

print(ord("a"))         #97
print(ord("A"))         #65
print(ord("z"))         #122
print(ord("Z"))        # 90

#Character to integer value

print(chr(90)) 

char = "n"
# upper()
print(char.upper())  # inbuilt method


# upper to lower
char = "D"
print(char.lower())  # inbuilt method


# using upper to lower 
ascii = ord(char)
print(ascii)
print(ascii + 32)
print(chr(ascii + 32))

#using lower to upper
char = "d"
ascii = ord(char)
print(ascii - 32)
print(chr(ascii - 32))

# upper to lower
char = "Z"
ascii = ord(char)
print(ascii + 32)
print(chr(ascii + 32))

############################################################
# logical operators

a = 10
b = 2
c = 4

# and 
 
print( a > b and a > c)         # T T = True
print(b > a and c > a)          # F F = False
print(c > a and c > b)          # F T = False

# or 
print( a > b or a > c)         # T T = True
print(b > a or c > a)          # F F = False
print(c > a or c > b)          # F T = True

# not 
print(not(a > b))          # False
print(not(b > c))          # True



###########################################################

# Perform bitwise operator

# identity Operators : is, is not

a = 10 
b = 10 

print( a == b)      # True
print(id(a))
print(id(b))

print(id(a) == id(b))

print( a is b)           #True
print( a is not b)      # False

x = [1,2,3,4,4,5,3]
print(x is 4)   #false

l = [10, 20, 30]
x = [10, 20, 30]

print(l is x)      # False
print(l == x)      # True

print( l is not x)   #True

#############################################################
# membership operators : in, not in 

t = (10,20,30,40,50,60)

print(10 in t)          #True
print(100 not in t)     #True

t = (10, 20, 30, 40, 50)
print(2, 4 + 3)
print(12, 10 in t)

print(89, 10, 30 in t)



