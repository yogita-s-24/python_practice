# dictionary  : is a collection of key-value pairs
# dictionary id mutable
# d = {k1: v1, k2: v2, k3: v3....}

s = {12,13,14,15,16}
print(len(s))

d = {"a": 10, "b": 20, "c": 30}
print(len(d))

#create the dictionary

d = {1: 10, 2: 20, 3: 30}
print(d)

#using classname 
d = dict({1: 10, 2: 20, 3: 30})
print(d)


#list of tuple

d = dict[("google", 92), ("apple", 112)]
print(d)

d3 = dict(a=1, b=2, c=3)
print(d3)

# empty dictionary
d4 = {}
print(d4)
print(type(d4))

d5 = dict()
print(d5)


###########################################
"""
characteristics of dictionary
1. cannot have multiple keys with same name
2. keys can only be one element
3. keys can only be immutable data (ind/string/tuple)
4. values can be of any data type
5. values can be accessed only through the keys
"""

d = {"a": 10, "b": 20, "c": 30, "a": 83}
print(d)

# composite keys
d = {(26, 1, 1) : "Republic day", (15, 1) : "independence day"}
print(d)

# d = {[1, 2]: "hello"}
# print(d)  # TypeError

d = {"a": [1, 2, 3]}
print(d)

d = {"Bangalore": 26, "Mysore": 23, "Chennai": 30, "Pune": 29}

# access the values of d
# var[key]

print(d["Bangalore"])
print(id(d))

print(d["Chennai"])
# print(d["Mumbai"])  # KeyError

# get()

print(d.get("Chennai"))
print(d.get("Noida", "key is not present"))
# print(d.get("Mumbai"))     #None

print(d.get("Bangalore", 1.2))

#####################################################################################

# adding new key value pairs

# d[key] = value

d["Mumabi"] = 90
print(d)

d.update({"Chennai": 30, "Delhi" : 4})

# setdefault()  # cannot be used to update the existing key value pairs
d.setdefault("Chennai", 25)
print(d)


######################################################################################
#fromkeys() - It will access only keys in the dictionary

l = ["a", "b", "c", "d"]
d1 = dict.fromkeys(l)
print(d1)

d2 = dict.fromkeys(l, 0)
print(d2)

#########################################################################################
# deleting keys and values from the dictionary

# pop()
# popitems()

d = {"Bangalore": 26, "Mysore": 23, "Chennai": 30, "Pune": 29}
print(d.pop("Mysore"))
print(d)

# print(d.pop("Mumbai"))    #KeyError
print(d.pop("Mumbai", -1))


# popitem - removes the last key value pair
e = {"Bangalore": 26, "Mysore": 23, "Chennai": 30, "Pune": 29}

print(e.popitem())
print(e)

#############################################################################################
# items() - return the key value pairs
# keys() - return the keys
# values() - return the values

x = {"Bangalore": 26, "Mysore": 23, "Chennai": 30, "Pune": 29}

print(x.keys())
print(x.values())
print(x.items())

################################################################################################
# merging the data types

s1 = "hai"
s2 = "hello"
print(s1 + s2)

l1 = [1, 2, 3]
l2 = [10, 20, 30]
print(l1 + l2)

print(*l1 , *l2)

t1 = (4, 5, 6)
t2 = (40, 50, 60)
print(t1 + t2)
print((*t1, *t2))

s1 = {1, 2, 3}
s2 = {4, 5, 6}
# print(s1 + s2)  # TypeError
print({*s1, *s2})

d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"d": 4, "e": 5, "f": 6}
# print(d1 + d2)  # TypeError

print({*d1, *d2})
print({**d1, **d2})

# dictionary cannot be index/sliced, unordered, not a sequence
