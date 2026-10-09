
#python tuples:tuple is the container to store multiple values in a same variable.
#()round bracket is used to create tuple. some examples:
num = (10,20,30,40)
names = ("shanti","sahkila","shamira", "shaira")
mixestypes = ("prem",24,75.5,True)
print(num[0])#output:10..tuples can be indexed and access by their index
print(names[-1])#output:shaira..python can be negative indexed where -1 start from the last element to first and can be accessed by negative index too.
print(len(names))#output:4, len()function gives the length of tuple
#in operator is used to check if any element is in the tuple or not
print("Shaina" in names)#output:False
print(names[1:4])#output:('sahkila', 'shamira', 'shaira'),,tupes can be sliced
for name in names:
    print(name)#output:shanti sahkila shamira shaira ...in vetically that is tuples element can be accessed using loop too
#count() method is used to count any element how many times it occour in a tuple
print(names.count("shaira"))#output:1...that is shaira element is only one in names tuple
#index() method is used to find index of any element in the tuple
print(names.index("shanti"))#output:0
#Tuple is used in the case when some data/elements is need not to change like
location = (28.3949, 84.1240)
days = ("Sunday", "Monday", "Tuesday", "Wednesday","Thursday","Friday","Satrurday")
months = ("January", "February", "March")
#tuple update: to update any tuple element value first we convert the tuple into a list and makes updates on that and then convert the list into tuple again, we cannot directly 
#update the vales of tuple beacuse the tuples are immutable or unchnaged
new_names = list(names)#converting tuple 'name' into tuple new_names
new_names[0] ="Shabita Bhabi"#updating list
names = tuple(new_names)#converting the list into tuple again
print(names)#output:('Shabita Bhabi', 'sahkila', 'shamira', 'shaira')
#Add items: tuples are immutable, it doesnot have the buit-in append() method to add items but some ways to add:
 #1. convert into list: first we cahange the tuple into list and then add items and convert to tuple
add_names = list(names)
add_names.append("Shabina")#adding new element into list
names = tuple(add_names)#converting list into tuple again
print(names)#output:('Shabita Bhabi', 'sahkila', 'shamira', 'shaira', 'Shabina')
 #2. add tuple to the tuple: python allows add tuple to the tuple so if we want to add one (or many) items create a new tuple and add it to the exixting tuple:
this_tuple = ("sarita","samina ")#creating a new tuple with two values
names += this_tuple#adding both tuples
print(names)#output:('Shabita Bhabi', 'sahkila', 'shamira', 'shaira', 'Shabina', 'sarita', 'samina ')
#remove items: to remove item from tuple we change tuple in list then remove item from list and aagin change the list into tuple
remove_names = list(names)
remove_names.remove("sarita")
names = tuple(remove_names)
print(names)#output:('Shabita Bhabi', 'sahkila', 'shamira', 'shaira', 'Shabina', 'samina ')
#Or you can delete the tuple completely, The del keyword can delete the tuple completely:
thistuple = ("apple", "banana", "cherry")
del thistuple
#print(thistuple) #this will raise an error because the tuple no longer exists
#Tuple Unpacking:creating tuple is tuple packing than storing the values/elements/items of tuples in the different variables is said the unpacking of the tuple.
#eg:
person = ("Prem",24,"Nepal")
name, age, country = person
print(name)
print(age)
print(country)
#the numbers of elements and variables we assigend must be equal or if we use asterisk to collect the remaining values as a list
#eg:
num = (10,20,30,40,50)
first, *middle, last = num
print(first)
print(middle)
print(last)#output:vertically,10 (in first line) [20, 30, 40] (in second line) 50 (in last line)
(one, two, *three) = days
print(one)
print(two)
print(three)#output:vertically..Sunday Monday ['Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Satrurday']
#Tuple Join: to join to or more tuples we use + operator
tuple1 = (1, 2, 3)
tuple2 = ("a", "b", "c")
tuple3 = tuple1 + tuple2
print(tuple3)#output:(1, 2, 3, 'a', 'b', 'c')
#if we want to multiply the content of the tuple then we can multiply the tuple by how many times we want to multiply the content
#eg:multiply the contents of tuple1 2 times
multuple1 = tuple1*2
print(multuple1)#output:(1, 2, 3, 1, 2, 3)
#eg: if we want to multiply the content of tuple2 3 times:
multuple2 = tuple2*3
print(multuple2)#output:('a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c')

 