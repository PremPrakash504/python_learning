#Python Collections (Arrays)
#There are four collection data types in the Python programming language:
#List is a collection which is ordered and changeable. Allows duplicate members.
#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
#Dictionary is a collection which is ordered** and changeable. No duplicate members.

# Python lists: list is the container to store multiple values in a same variable. list is one of 4 built in data types used to store collections of data,
# the other three are tuple, set and dictionary, all with d3ifferent qualities and useage.
#lists are creqated using square bracket[]
students = ["ram","shyam","hari","sita"]
print(students)
print(students[0])#output: ram
#lists items are ordered, changabele and allow duplicate values.
#ordered: when we say that lists are ordered it means that the items have defined oredr, and the order will not changed, if new item is added then it will placed at the nad of the list items.
students[2] = "gita"
print(students)# output:['ram', 'shyam', 'gita', 'sita'], where indexed value 2 "hari" is changed by "gita"
students = ["ram","shyam","hari","sita","ram"]
print(students)#output:['ram', 'shyam', 'hari', 'sita', 'ram'], lists allows dulipcate values
print(len(students))#output:5, give the length of list
# lists items can be of any data types
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
# a list can contain any data type with strings, integers, boolean values
list4 = ["abc", 34, True, 40, "male"]
#type(): lists are defined as objects with the data type'list'
print(type(list1))#output:<class 'list'>
print(type(list2))#output:<class 'list'>
print(type(list4))#output:<class 'list'>
#append(): this function is used to add new item to the list which is placed at the end of the list
list1.append("graphes")
print(list1)#output:['apple', 'banana', 'cherry', 'graphes']
#insert: this function is used to insert item at the specific position of list
list1.insert(0,"Papaya")
print(list1)#output:['Papaya', 'apple', 'banana', 'cherry', 'graphes']
#remove():this function is used to remove any items by giving value
list1.remove("cherry")
print(list1)#output:['Papaya', 'apple', 'banana', 'graphes']
#pop(): this function is used to remove items by index from list
list1.pop(0)
print(list1)#output:['apple', 'banana', 'graphes']
#pop() function defult remove the last item
list1.pop()
print(list1)#output:['apple', 'banana']
#in: is used to check whether the item is in list or not return true if item is in list
print("apple" in list1)#output:true
#list slicing: some of the part of the list can be extracted
numbers= [50,40,30,20,10]
print(numbers[1:4])#output:[50, 40, 50]
#sort(): lists can be sorted ascending order
numbers.sort()
print(numbers)#output:[10, 20, 30, 40, 50]
numbers.sort(reverse=True)#to sort numbers in decending order
print(numbers)#output:[50, 40, 30, 20, 10]
students.reverse()#to reverse the list from last to first
print(students)#output:['ram', 'sita', 'hari', 'shyam', 'ram']
for student in students:# using for loop to access the lists items orderly in vertically
    print(student) 
