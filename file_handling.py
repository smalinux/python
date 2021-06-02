# -------------------
# -- File Handling --
# -------------------

#import os
#print(os.getcwd())
#print(os.path.dirname(os.path.abspath(__file__)))

file = open("./tmp.txt", "r")

# file info
print(file.name)
print(file.mode)
print(file.encoding)

#print(file.read()) # read all file
#print(file.readline())
#print(file.readlines())



for line in file:
    if line.startswith("cat"):
        break
    print(line)

file = open("./tmp.txt", "a") # append
#file = open("./tmp.txt", "w") # write

x = 10
while x > 0:
    file.write(f"{x}")
    x -= 1


print(file.tell()) # place of curser
file.seek(20)
file.write("fu")

file.close()
