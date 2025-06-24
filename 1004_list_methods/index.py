# adding element to the list

# append - add element at the end

# insert - add element at the specific index

# extend - add element at the end

li = ['geeks']

# use method
li.append('for')
li.append('geeks')

# display list
print(li)


li = ['geeks', 'geeks']

# use method
li.insert(1, 'for')

# display list
print(li)


#####################################################################
name = ["ram", "shyam", "hari"]
name.append("Sita")
print(name)

# append methos will add the element to the ens of the list

name = ["ram", "shyam", "hari"]
name.insert(2, "Gita")
print(name)

# insert method is used to add the element at the specific index

name = ["ram", "shyam", "hari"]
name.extend(["Rina", "Tina"])
print(name)

#extend method is used to add the multiple elements in the list

#######################################################################
# methods for the removing the elements from the string 

# pop 
# remove
# clear()

num = [1,2,3,4,5]
num.pop()
print(num)

num = [1,2,3,4,5]
num.pop(2)
print(num)

# pop method is used to remove the element from the list from the last index 
# but we can also pass the index value which we wants to remove 

number = [10,20,30,40,50]
number.remove(40)
print(number)

# remove method is used to remove the element from the list
# but we wants to pass the value of the element which we wants to remove it (not the index)

num2 = [100, 200, 300, 400]
num2.clear()
print(num2)

# clear method is used to remove all the elements from the list and it will print the empty list 

############################################################################################################\
# copy() - shallow copy
# copy method is used to copy the list to the one list to another list

num = [1,2,3,4,5]
num1 = num.copy()
print(num)
print(num1)

################################################################################################################

# sort() -

num5 = [45,39,29,98,49,35,78]
num5.sort()
print(num5)

num5.sort(reverse=True)
print(num5)

#################################################################################################################

# index(element) : return the index value

word = "HelloWorld"
print(word[0])
print(word[4])
print(word[3])
print(word[6])


# count(element) : number of occurrences
print(word.count("o"))
print(word.count("l"))

##################################################################################################################
# slicing -  

# perform the slicing on the list
print(word[2:5])

# slicing - [start:end:step] - 
# start - start index value
# end - end index value
# step - step value - step value is optional

