#
# data types
#
# type()

name = "Sohaib"
age = 55
tall = 1.5
long_num = 1000000000000000000000000000000000000000000000000000000
long_num += 1
sma_list = [1,2,3,4,5]
sma_tuple = (1,2,3,4,5)
sma_dect = { "one": 1, "two": 2, "three": 3}

print(type(name), name)
print(type(age), age)
print(type(tall), tall)
print(type(long_num), long_num)
print(type(sma_list), sma_list)
print(type(sma_tuple), sma_tuple)
print(type(sma_dect), sma_dect)
print(type(2 == 2))
print(type(2 == 4))

# re-assing var

x = 33
x = "hello"


print(x)

a, b, c = 1, 2, 3

print(a)
print(b)
print(c)

# scape in python "\" not "\n"
print("line 1 \
line 2 \
line 3")

# line feed
print("line\n feed")

# print hex
print("\x74")
