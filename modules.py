import random
import sys
import smalinux as ee # ee == name space

# from module import specific functions
from random import randint

print(random) # print info about the module

# show all info from any module
print(dir(random))

print("=" * 50)

sys.path.append(".")
print(sys.path)

print("=" * 50)

def main():
   print("{}".format(random.random()))

   print("{}".format(randint(1, 100)))

   #smalinux.Hi()
   ee.Hi()


main()


# pip - python package manager
#   pypi.org
# pip manual: https://pip.pypa.io/en/stable/
#
#
#
#
#
#
#
#
#
#
#
