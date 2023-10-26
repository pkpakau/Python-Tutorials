# String Methods

text = "Hello World"

print(len(text))

for t in text:
    print(t)

print("\n")
print(text[6:])

# len for list or string( sequence of characters )
print(len(text))

# slice ( start, end, step )
print(text[6:-1:2])

# escape characters 
# \n - new line
# \t - tab
# \b - backspace
# \s - space
# others - google them when required

# string formatting
# name = input()
# age = int(input())

# print("My name is " + name + " and I am " + age + " years old!")
# print("My name is %s and My Age is %d years old!" % (name, age))
# print("My name is {} and my age is {} years old!".format(name, age))

# Case Manipulation Functions
text = "This is my text!"

print(text.upper())
print(text.lower())

print(text.title()) # capitalize every world
print(text.swapcase()) # Swap the case ( lower to upper, upper to lower )

text = "I am Mike and my life is beautiful! Because of my job!"
print(text.count("my")) # count occurence of string

print(text.count(" ")) # count spaces

# find(<substring>) - returns the index of substring
text = "I am Mike and I feel great!"

print(text.find("Mike"))

# join(<sequence or string>)
seperator = ";"
mylist = ["Kitchen", "Dog", "Mike"]

newstr = seperator.join(mylist)
print(newstr)

# split(list or string)
splitted_string = text.split("a") # default <space> as delimiter
print(splitted_string)

# replace function

print(text.replace("Mike", "Parag"))