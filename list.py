#
# list
#

def list_methods():
    myFiends = ["sohaib", "ahmed"]
    # append
    myFiends.append("ali")
    print(myFiends)
    myFiends.append(["one", "two", "three"])
    print(myFiends)
    print(myFiends[3][0]) # one

    # extend
    list2 = ["one", "two", "three"]
    myFiends.extend(list2)
    print(myFiends)

    # remove
    myFiends.remove("sohaib")
    print(myFiends)

    # sort
    lis = [9,7,4,2,3,1,5,6,8,0]
    lis.sort()
    print(lis)

    lis.sort(reverse=True)
    print(lis)

    # reverse()
    lis = [9,7,4,2,3,1,5,6,8,0, 999, 999, 999]
    lis.reverse()
    print(lis)

    # clear() & copy()
    b = lis.copy()
    lis.clear()
    print(lis)
    print(b)

    # count
    print(b.count(999))

    # index
    lis = [9,7,4,2,3,1,5,6,8,0, 999, 999, 999]
    print(lis.index(999))

    # insert
    lis.insert(0, 1000)
    print(lis)

    # pop
    lis.pop(-1)
    print(lis)

def main():
    myList = ["one", 1, 100.7, True]
    print(myList)
    print(myList[0])
    print(myList[0:2])
    print(type(myList[1])) # int
    print(type(myList[2])) # float

    myList[1] = "two"
    print(myList[1]) # int
    print(type(myList[1])) # int

    myList[1] = [1,2,3,4,4]
    print(myList) # ['one', [1, 2, 3, 4, 4], 100.7, True]


    #######################
    list_methods()
    ###################################

    print("=" * 50)

    my_list = [3] * 50
    print(my_list)

    ls2 = [1,2,3,4,5,6,7]
    print(ls2[1:4]) # from 1 to less than 4
    A = ls2 * 3
    print(A)
    print(ls2)
    ls2[2] = 44444
    print(A)
    print(ls2)
    ###################################

    ls22 = []
    for i in range(10):
        ls22.append(i)

    print(ls22.pop(9)) # index
    print(ls22.count(8))
    #print(ls22.reverse(0))

    print((22).__add__(44))

    while ls22:
        print(ls22.pop(), end='')

    ###################################
    print("=" * 50)

    ls33 = list(range(10))
    print(ls33)


main()
