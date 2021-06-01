
def say_hi(*people):
    for name in people:
        print("hi {}".format(name))

def add(a, b):
    return a +b

def main():
    x = add(4, 2)
    print(x)

    say_hi("Sohaib", "ali", "ahmed")


main()
