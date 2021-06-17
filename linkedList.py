class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None
    def get_data(self):
        return self.data
    def get_next(self):
        return self.next
    def set_data(self, new_data):
        self.data
    def set_next(self, new_next):
        self.next = new_next

class UnorderedList:
    def __init__(self):
        self.head = None
    def is_empty(self):
        return self.head == None
    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count +=1
            current = current.get_next()
        return count
    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found

temp = Node(93)
print(temp.get_data())

t2 = Node(93)
temp.next = t2
#print(temp.next())

mylist = UnorderedList()
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(54)

print(f"{mylist.head.data}") #54
print(f"{mylist.head.next.data}") #93
print(f"{mylist.head.next.next.data}") #17
print(f"{mylist.head.next.next.next.data}") #77
print(f"{mylist.head.next.next.next.next.data}") #77

print("=" * 50)

print(mylist.size())
