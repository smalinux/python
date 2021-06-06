import time

def sum_of_n(n):
    start = time.time()

    the_sum = 0
    for i in range(1, n+1):
        the_sum = the_sum + i

    end = time.time()

    # WTF, function in python returns more than one value...
    return the_sum, end-start # return a tuple

def main():
    v = sum_of_n(5) # v is a tuple
    print(type(v)) # tuple
    print(v)

main()
