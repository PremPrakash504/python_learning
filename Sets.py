
#Python Sets:Sets is used to store multiple values in single variable that does not stores duplicate value
# It is collection which is unordered, unchangeable and unindexedable.
#Unordered means that the items in a set do not have a defined order.
#Set items can appear in a different order every time you use them, and cannot be referred to by index or key.
#Set items are unchangeable, meaning that we cannot change the items after the set has been created.
#Once a set is created, you cannot change its items, but you can remove items and add new items.
# curly bracket is used to create sets
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)#output:{'banana', 'apple', 'cherry'}
#duplicates not allowed in sets, sets cannot have two items with the same value, duplicates value will be ignored
#the values true and 1 are considered as the same value in sets and are treated as duplicates
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)#output:{True, 2, 'cherry', 'banana', 'apple'}
#the values false and 0 are considered as the same value in sets and sets treated them as duplicate value
#len() function is used to get the length of the set
print(len(thisset))#output:5
#sets items can be any data types
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
#A set can contain different data types:
set4 = {"abc", 34, True, 40, "male"}
#type() is used to check the data type of set and python defined sets as objects with data type set
print(type(set1))#output:<class 'set'>
print(type(set4))#output:<class 'set'>
#set() constructor is used to make or create set, eg;
myset = set(("nepal","china","india"))# two round barcket is used where no curly bracket is used here
print(myset)
#Access Item: as sets are unindexedable we cannot access its elements using the indexing, but we can access through for loop or ask if any element present using in keyword. 
for x in myset:
    print(x)
#check if nepal is present in myset
print("nepal" in myset)#output:true
#check if india is not present in myset
print("india" not in myset)#output:false
#check if japan is not in the myset
print("japan" not in myset)#output:true
#change items:as the sets are unchangeable, once set is created we cannot change its items but we cann add new items using add() method
myset.add("america")
print(myset)#output:{'nepal', 'china', 'america', 'india'}
#addsets:to add items from one set into the another set we use upadte() method
myset.update(set1)
print(myset)#output:{'china', 'india', 'cherry', 'america', 'banana', 'nepal', 'apple'}
# add any iterable: in update() method we can pass any set, list, tuple, dictionary
mylist = ["one","two"]
set2.update(mylist)
print(set2)#output:{1, 3, 'one', 5, 'two', 7, 9}
set3.update(("nepali","hindi"))
print(set3)#output:{False, True, 'nepali', 'hindi'}
#remove items: to remove items from the sets we use remove() or the discard() method
myset.remove("banana")
print(myset)#output:{'apple', 'cherry', 'china', 'nepal', 'america', 'india'}
#remove() method will raise an error if the item to remove does not exist
myset.discard("apple")
print(myset)#output:{'america', 'cherry', 'nepal', 'china', 'india'}
#discard() method will not raise the error if the item to disacred does not exist
#pop() method: this method remove or pooped a item randomly from the sets as the are unordered or unindexed so the items are randomly popped
y = myset.pop()
print(y)#output:cheery
print(myset)#output:{'america', 'nepal', 'india', 'china'}
cities = {"kphplpur","nepalgunj"}
#clear() method is used to empties the set:
cities.clear()
print(cities)#output:set()
#del keyword delete the set completely
del cities
#print(cities),, and this will show an error

#Join Sets: There are several ways to join two or more sets in python.
#a. union() or | operator: method returns a new set with all items from both sets.
setone = {"a","b","c","d"}
settwo = {1,2,3,4}
setthree = setone.union(settwo)
print(setthree)#output:{'a', 1, 2, 3, 4, 'd', 'b', 'c'}

