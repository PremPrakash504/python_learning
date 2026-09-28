#1 python strings
name = "Prem Prakash"
print(name[0:4])
print(name[0:])
print(name[:10])
print(name[:-7])
print(name[-7:])
print(name[0:11:2])
print(name[::2])
print(name[::-1])
print(name.upper())
print(name.lower())
Name = " Trippie Alon "
print(Name.strip())
print(Name.replace("Alon","Redd"))
print(name.split(" "))
data = "ram shyam hari"
print(data.split(" "))
let = "apple ball"
print(let.capitalize())
print(let.title())
print(name + " " + Name)
age = 24
print(f"My name is {name} and I am {age} years old.")
city = "Nepalgunj"
print(f"My name is {name} and i am  {age} years old and ia lives in {city}.")
price = 100
quantity = 5
print(f"total = { price*quantity}")
print("My name is {} and i am am {} years old.".format(name,age))
print("My name is{0} and i am {1} years old.".format(name, age))
print("maai name is %s and i am %d years old ." %(name,age))

#2 python boolens
x = True
y = False
print(x) # output true
print(type(x)) # output: boolean
print(y)
print(type(y))
a = 3; b = 2
print(a>b)# output: True
print(a==3) #output: True
print(b==7) #output: false
print(name== "Prem Prakash") # we can also compare strings and the output is true 
print(name=="ramesh") # and the output is false 
print(name=="prem Prakash")# also strict on capital letters and the output is false
  #bool() function:  integer or strings value if we give in bool function then it give true as output
  # and if we give 0 or empty string it will give false as output
print(bool(0)) # output:false
print(bool(1)) #output: true
print(bool(2)) # output: true
print(bool("hello")) # non empty string and output true
print(bool(""))# empty string and output is false
print(bool([1,2,3]))# non empty list aan dthe output is true
print(bool([]))# empty list and the output is false
print(age >= 18) # output: true

#3 Python Operators : these are the symbols that are ussed to any operation in python
   # A. Arthemetic operators: these are used forr calculations 
i = 2; j = 3
print(i+j)# Addition Operator an output is 5
print(i-j)#Subraction Operator and output is -1
print(i*j)# Multipication output 6
print(i/j)#division output 0.666...
print(i%j)# modululus or reminder, output 2
print(i**j)#power,output 8
print(i//j)# floor division value output 0

#B. assignment operator: is used to assign values to the variable
z  =2; # assigning value to variable 
z+=1; # internally z=z+1
print(z)# output: z=2+1 = 3
z-=1
print(z)#output:z=z-1=3-1=2
print(z)
z*=3
print(z)#output:z=z*3=2*3=6
z/=2
print(z)#output:z=z/2=6/2=3
z%=2
print(z)#output:z%2=3%2=1

#C. Comparision Operator: is used to compare to values and return true and false
p=10; q=9
print(p==q)#output:false
print(p==10)#true
print(p!=q)#true
print(p>q)#true
print(p<q)#false
print(p>=q)#true
print(q<=p)#true
#python allows us to chanin comparision opeartors
print(1<p<16)#true
print(8<=q and q <=10)#true
#D. Logical operators: is used to combine multiple conditions 
  #and: return true if both conditions are true
age = 24
print(age>=18 and age <=30)# true
  #or: return true if only one of the condition is true or match
print(age>=20 or age <= 20)#true
  #not:reverse the boolean result
print (not age) # age output recently was true and now became false
#E. Idenity Operator:identity opeartors are used to compare the objects, not only if they are equal, but they are actually the same object with the same memory location
 #is : is operator is usde to return true if both variable point to the same object
c = ["apple", "banana"]
e = ["apple", "banana"]
f= c

print(c is f)#true
print(c is e)#false
print(c == f)#true
#is not: is not operator return true if the both variables do not point to the same object
print(c is not e)#true
print(c is not f )#false

#F.MemberShip Operator: is to test if any sequence of value is present in object
 #in: return true if a sequence with the specified value is present in the object
print("banana" in c)#true
print("orange" in c)#false
# not in: returns true if a value is not in object
print("orange" not in c)#true

#G Bitwise Operator: is used to compare(binary) numbers
