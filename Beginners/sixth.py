### Sequences and Collections

print("List tutorials")
mylist = [10, 20, 30]
print(mylist)
print(type(mylist))

mylist = [10, "hello", True]
print(mylist)

print(mylist[0], type(mylist[0]))
print(mylist[1], type(mylist[1]))
print(mylist[2], type(mylist[2]))

# print(mylist[3], type(mylist[3])) 
# above will give out of bound exception

mylist = [ 10, 20, 30, "string", True, 8.97]
# variable[start:end+1:step]
print(mylist[:5:2])

# negative step
print(mylist[-2])

mylist[3] = 6.54
print(mylist)

print("\nIterate items in list through for loop")

for x in mylist:
    print(2 ** x)

# Append list
x = [1, 2, 3]
y = [4, 5, 6]

print( x + y )

# Multiple list by scalers
print(x * 3)

# Min Max
# x = [1, 2, 3, "hello", True]
x = [1, 2, 3]
print(len(x))
#print(min(x)) # doesn't work for str and int/float comparison

print(min(x))
print(max(x))

# Append Method
print("Append Method")
x = [1, 2, 3, "hello", True]
x.append(10.23)
         
# insert method
x.insert(3, "fourth element")
print(x)

# remove method
x.remove("fourth element")
print(x)

# pop method
x.pop(3) # pop at index mentioned

print(x)
# print index if element exist
x.pop(x.index(10.23))
print(x)

# Sort method ( x.sort() or sorted(x) )
x = [55, 6, 1, 99, 2, 3]
print(x)
# x.sort() # sort the list
# print(x)
sorted(x) # only sort while displaying or printing ( doesn't change the list )
print(x)



### Tuple (immutable)
print("\n\n Tuple Codes!!!")
x = [10, 20, 30]
y = (10, 20, 30)

# y[1] = 100 # not possible ( immutable )
# if want to mutate
print(x)
x = list(x)
x[2] = 40
x = tuple(x)

print(x)


### Dictionaries
person = {
    'name': 'Parag Khuman',
    'age': 25,
    'gender': "male",
    True: 99
}
print(person)

# person[0] - doesn't work ( as not indexed, must be access by key)
print(person['name'])
print(person[True])

person['age'] = 24
print(person)

# imp method ( items, keys, values )
print(person.items())
print(type(person.items()))
print(person.keys())
print(person.values())

### Membership Operators
# ( not, not in )
print("\n\nMembership Operators")
x = [1, 2, 3]
print(2 in x)
print(4 in x)

### Identity Operators
#( is, is not )
x = "hellos"

print("\nIdentity Operators!")
if type(x) is int:
    print("x is int")
else:
    print("x is not int")