#
# tuples
#

def tuple_methods():
    print("hello")

def main():
    tpl = ("one", "two", "three")
    tpl2 = "one", "two", "three"
    print(type(tpl))
    print(type(tpl2))
    #######################
    tuple_methods()

    ##########################
    tpl22 = ("one", ) # tpl with one element
    tpl23 = "one",   # tpl with one element
    print(type(tpl22))
    print(type(tpl23))
main()
