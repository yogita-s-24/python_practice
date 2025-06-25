# typecasting = process of converting / changing from one data type to another

# string = '' , "", """ """, str()

word = "hai"
number = "123"
decimal = "18.53"

#string to interger

# print(int(word))     #ValueError 
# cannot convert the string to the integer
print(int(number))      #123

# string to float
# print(float(word))      #ValueError 
print(float(number))    #123.0
print(float(decimal))    #18.53

# string to boolean
word = "hello"
word1 = "  "
word2 = ""

print(bool(word))
print(bool(word1))
print(bool(word2))

# string to list
word = "hello world"
print(list(word)) # ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
print(word.split())  # ['hello', 'world']

#string to tuple
word = "Hello World"
print(tuple(word))

#string to set
word = "Hello"
print(set(word))

# string to dictionary
word = "hello"
# print(dict(word))  # ValueError
print(dict.fromkeys(word, 0))     #{'h': 0, 'e': 0, 'l': 0, 'o': 0}
print(dict.fromkeys(word))        # {'h': None, 'e': None, 'l': None, 'o': None}

