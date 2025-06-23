# tuple is a collection of datatype
# immutable datatype

# all are individual datatype, string, tuple = immutable datatype

boundary = (1,2,3,4,5)
print(boundary)

# creating a tuples
t = (1, 2, 3, "hai", [10, 20])

# using class name
t1 = tuple((1, 2, 3))  # tuple()

# to store 1 element in tuple
t2 = ("hello", )

# empty tuple
t3 = ()
t4 = tuple()

#################################################
l = [10, 20, 30]
l[0] = 100
print(l)

# t = (100, 200, 300)
# t[0]= 500
# print(t) # TypeError   # immutable

#####################################################
t = (10, 20, 30, 40, 50)
print(len(t))

#tuple methods

# count()
t = (1, 2, 3, 4, 5, 1, 2, 3)
print(t.count(1))
print(t.count(10))

# index()
t1 = ("hai", "hello", "world", "python")
print(t1.index("hello"))
# print(t1.index(1))  # ValueError
# print(t1.index("google")) # ValueError


# perform the slicing on tuples
t2 = (1, 2, 3, 4, 5)
print(t2[1:4])


