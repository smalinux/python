# pip - python package manager
#   pypi.org
# pip manual: https://pip.pypa.io/en/stable/
####################################
# Modules can import other modules
####################################
# Google: import importlib
####################################
#
#
#
#
#
#
#
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

def love_fun():
    pass

def main():
   print("{}".format(random.random()))

   print("{}".format(randint(1, 100)))

   #smalinux.Hi()
   ee.Hi()
   print(love_fun.__name__)
   print(ee.__name__)

   # assign module function to a local name
   # If you intend to use a function often you can assign it to a local name:
   hyx = ee.Hi

   hyx()
   hyx()
   hyx()
   hyx()
   hyx()

   #########################################################

main()


