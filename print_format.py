# print format
# ==================
#
# read more about python format
#               https://pyformat.info/
#
#
#
#
#

# C style format - tha old way
def c_style_format():
    name = "Sohaib"
    age = 27
    rank = 100

    print("My name is: %s and age: %d and my rank %f" % (name, age, rank))


    # control floating point number
    print("My number is: %.2f" % rank)

    # %.5s
    str = "Sohaib Mohammed bla bla"
    print("%s" % (str))
    print("%.5s" % (str)) # first 5 char only


def new_ways():
    name = "Sohaib"
    age = 27
    rank = 100
    str = "Sohaib Mohammed 2222"
    money = 56756756755564564

    print("my name is {}" .format(str))
    print("my name is {} {} {}" .format(str, str, str))
    print("My name is: {} and age: {} and my rank {}".format(name, age, rank))
    print("My name is: {:s} and age: {:d} and my rank {:.2f}".format(name, age, rank))
    print("{:.5s}".format(str)) # first 5 char only

    print("my money in bank is: {}".format(money))
    print("my money in bank is: {:_}".format(money))

    a, b, c = "one", "two", "three"

    print("hello {} {} {}".format(a, b, c))
    print("hello {2} {1} {0}".format(a, b, c))

    a, b, c = 10, 20, 30

    print("hello {2:.2f} {1:.3f} {0:.6f}".format(a, b, c))


    # Python 3.7+
    print(f"my name is {name} and my age: {age}".format(name, age))

def main():
    c_style_format()
    new_ways()
main()
