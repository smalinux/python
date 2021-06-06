# range()

str1 = "Sohaib Mohmmed"

for x in str1:
    print(f"{x}", end=" ")

print("="*50)
########################################################

words = ['cat', 'dog', 'caw']

for c in words:
    print(f"{c[0]} = {len(c)}")

print("="*50)
########################################################

for i in range(6):
    print(f"{i}", end=" ")

print("="*50)

for i in range(2, 10, 2):
    print(f"{i}", end=" ")
########################################################

def xxx():
    print("hello")

xxx()
