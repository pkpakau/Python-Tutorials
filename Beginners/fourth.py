# Lec4 : If statements and conditions
x = input('First Number: ')
y = input('Second Number: ')

x = int(x)
y = int(y)

if x < y:
    print("x is less than y!")
    if x >= 0:
        print("x is positive!")
    else:
        print("x is negative")
elif x > y:
    print("x is greater than y!")
    if x > 100:
        print("x is greater than 100!")
else:
    print("x is equal to y!")