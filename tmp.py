

def tmp():
    print("=" * 50)
    print("#$%$#=" * 50)

    print(20 > 3 and 20 < 100)
    print(20 > 3 or 20 < 100)

    print(not(20 > 100))

    #--------------------------

    i = 5
    print(i)


    # convert int to str
    i = str(i)
    print(type(i))
    print(i)


    fName = input("what's your name?")
    Email = input("Email?")
    username = Email[:Email.index("@")]
    website = Email[Email.index("@")+1: ]
    fName = fName.strip().capitalize().upper()
    print("Hello, {}".format(fName))
    print("username: {}".format(username))
    print("website {}".format(website))


    age = input("age?")
    age = int(age)
    print(type(age))


tmp()
