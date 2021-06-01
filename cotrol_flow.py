def main():
    if 30 < 20: print("30 > 20")
    elif 444 > 0: print("444 > 0")
    else: print("50 > 20")


    if 10 <= 10:
        print("<=")

    name = "Sohaib"
    print("X" in name) # False
    print("S" in name) # True
    print("Z" not in name) # True


    i = 10
    while i > 0:
        print(i)
        i -= 1
    else:
        print("loop is done")


    lis = [1,2,3,4,5,6,66,77]

    for i in lis:
        if i == 3:
            continue
        elif i == 5:
            continue
        elif i == 66:
            break
        print(i)
    else:
        print("for loop is finished")


main()
