import random

# from module import specific functions
from random import randint


print(random) # print info about the module

# show all info from any module
print(dir(random))

print("=" * 50)

def main():
   print("{}".format(random.random()))

   print("{}".format(randint(1, 100)))


main()
