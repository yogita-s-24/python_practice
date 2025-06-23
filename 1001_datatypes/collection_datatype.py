"""
collection datatypes
1. strings (str)
2. lists (list)
3. tuples (tuple)
4. sets (set)
5. dictionary (dict)
"""

#string : collection of characters
#list : collection of items
#tuple : collection of items
#set : collection of unique items
#dictionary : collection of key-value pairs

# length of string : len()
word = "hello world"
print(len(word))

word = " "
print(len(word))

##################################################################
# raw strings : r/R

sentence = "hai welcome to python class"
print(sentence)

sentence = "hai welcome \to pytho\n class"
print(sentence)

sentence = r"hai welcome \to pytho\n class"
print(sentence)


###########################################
# memory address of an object

word = "hai"
print(id(word))

word = "hello"
print(id(word))

#########################################
# indexing : process of extracting 1 element at a time
# index starts from 0

word = "python"
print(word[0])
print(word[4])

word = "hello world"
print(word[6])
print(word[3])

sentence = "python programming"
# extract the char of t, n, m, g

word = "hello"
# to extract the first char : variable[0]
# to extract the last char : variable[len(var)-1] / variable[-1]

print(word[0])

print(len(word))
print(word[5-1])
print(word[4])

word = "hello"
print(word[-1])