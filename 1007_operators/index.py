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