from collections import deque
# lists - tuple - namedtuples - sets - Dictionaries -




##################### list
x = []
print("append()")
x.append(4)
x.append(5)
x.append(6)
print(x)

print("extend")
tmp = [3,33,333]
x.extend(tmp)
print(x)

print("insert(0, 555)")
x.insert(0, 555)
print(x)

print("remove(5)")
x.remove(5)
print(x)

print("pop")
x.pop()
print(x)

print("pop(0)")
x.pop(0)
print(x)

print("clear")
x.clear()
print(x)

##################### queue

queue = deque(["Sohaib", "Mohammed", "ali"])
queue.append("ola")
print(queue)
print(queue.popleft())
print(queue.popleft())
print(queue)

#########################
for x in range(10):
    print(x)


#########################
# python tutorial - 5.1
print("list 1:")
lis1 =[(x,y) for x in [1, 2, 3] for y in [3,4,5]  if (x != y)]
print(lis1)

comp = []
for x in [1,2,3]:
    for y in [3,4,5]:
        if x != y:
            comp.append((x,y))
print(comp)

######################### del
a = [x for x in range(20)]
del a[1:3]
del a[:]
a = [x for x in range(20)]
del a[5]
del a

######################### Tuples
t = 12, "love", "free", 3.5
print(t[0])
print(t[1])
print(type(t))

######################### Sets


#########################
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
print(sorted(set(basket)))


#########################
if 4 == 4:
    print("Ok")


