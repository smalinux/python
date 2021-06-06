
# Default Arg Values
def ask_ok(prompt='', retries=4, reminer='Please try again!'):
    '''Python Tutorial, 4.7.1 Default Argument Values'''
    while True:
        ok= input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries -1
        if retries < 0:
            raise ValueError('invalid uuser responnse')
        print (reminer)


def say_hi(*people):
    for name in people:
        print("hi {}".format(name))

def add(a, b):
    return a +b

# L == static local in C language
def f(a, L=[]):
    if L is None:
        L = []
    L.append(a)
    return L


def rec(a):
    ''' minimal recirsion function'''
    print(a, end=' ') # every step action

    if a == 0: # end condition
        return 0

    return rec(a - 1) # decrement/increment

def cheeseshop(kind, *arguments, **keywords):
    # *x == tuple
    # **x ==  dictionary
    pass

def main():
    x = add(4, 2)
    print(x)

    say_hi("Sohaib", "ali", "ahmed")

    ##########################################################
    x = ask_ok()
    if x:
        print ("nice :)")
    else:
        print ("bad :(")

    ##########################################################
    print(f(1))
    print(f(2))
    print(f(3))
    print(f(50, None))
    print(f(1))
    print(f(50))
    print(f(33))

    ##########################################################
    rec(5)
    print('')

    ##########################################################










main()
