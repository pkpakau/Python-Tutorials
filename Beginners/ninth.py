# File Operations

# open(<file>, modes) # Modes - r, w, a
# Every opened stream should be closed ( open and close mandatory)

file = open('myfile.txt', "r")
file.flush() # flush the stream but doesn't close the stream( while consecutive write present code) 
file.close() # flush and deletes the stream

# another method ( doesn't require to close the stream )
with open("myfile.txt", "r") as f:
    content = f.read()

print(content)


# Writing
with open("myfile.txt", "w") as f:
    f.write("Hello, Github")
    

file = open("myfile.txt", "r")
content = file.read()

try:
    # stream code
    file = open("file.txt", "a")
    file.write("\nFrom append in try except")
except:
    # catch
    # pass
    print("Error while reading files")
finally:
    # close the stream
    # pass
    file.close()
    