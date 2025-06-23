"""
datatypes : type of data stored in container

2 types of data types
1. individual data type / single value data type
2. collection data type / multi value data type

Individual data type
1. integers (int)
2. floats (floats)
3. boolean (bool)
4. complex (complex)

collection data type
1. strings (str)
2. lists (list)
3. tuples (tuple)
4. sets (set)
5. dictionary (dict)
"""


# remove/truncate the decimal part

y = 2.684
print(int(y))

# bool class is used to check the emptiness of any data type
# integers
x = 10
print(bool(x))


# default value of integers : 0 / int(0) / int()

#####################################################################

import math 
print(math.trunc(y))

print(round(y))

a = 1 + 2j
print(a)

a = complex(0)
print(a)



##########################################################

# float
c = 1.2
print(bool(c))


# default value of floats : 0.0 / float(0.0) / float()

##########################################################
# complex number

c = 1 + 2j
print(bool(c))

c = 1 + 0j
print(bool(c))

c = 0 + 0j
print(bool(c))

print(bool(0j))

print(bool(complex(0j)))