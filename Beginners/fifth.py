### Lec 5 : While and For Loop

x = 0

while x < 10:
    x += 1
    print(x)

# while True:
#     print("test infinite loop")

# For Loop
# range(start, stop, step)
for x in range(1,21, 2):
    print(x)

# 1
# 3
# 5
# 7
# 9
# 11
# 13
# 15
# 17
# 19

## Loop Control Statements
x = 0
print("Loop Control Statements")
while x < 10:
    if x == 5:
        break
    x += 1
    print(x)

print("Continue Example")
while x < 10:
    x += 1
    if x == 5:
        continue
    
    print(x)

# Pass Statement ( Fill places where code is needed but temporarily put something )
print("Pass Statement")
if x == 25:
    pass