import timeit
from timeit import Timer


# Best 4
def test1():
    l = []
    for i in range(1000):
        l = l + [i]


# Best 3
def test2():
    l = []
    for i in range(1000):
        l.append(i)


# Best 2
def test3():
    l = [i for i in range(1000)]


# Best 1
def test4():
    l = list(range(1000))



def main():
    t1 = Timer("test1()", "from __main__ import test1")
    print("concat ", t1.timeit(number=1000), "milliseconds")

    t2 = Timer("test2()", "from __main__ import test2")
    print("append ", t2.timeit(number=1000), "milliseconds")

    t3 = Timer("test3()", "from __main__ import test3")
    print("comprehension ", t3.timeit(number=1000), "milliseconds")

    t4 = Timer("test4()", "from __main__ import test4")
    print("list ", t4.timeit(number=1000), "milliseconds")

    #x = list(range(2000000))
    #pop_zero = Timer("x.pop(0)", "from __main__ import x")
    #pop_zero.timeit(number=1000)

    #x = list(range(2000000))
    #pop_end = Timer("x.pop()", "from __main__ import x")
    #pop_end.timeit(number=1000)

main()
