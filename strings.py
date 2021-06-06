# strings immutable == cann't modified
#
# concat
# can't concat string & number.. should convert it to string first
# single and double quotes

def concat():
    str1 = "I'm"
    str2 = "Sohaib"
    msg = str1 + " " + str2

    # concat
    print(msg)

    b = "a\
b\
c"

    name = """
one,
two,
three

"""

    print(b)
    print(name)
    print(b + name)

def single_double():
    str1 = 'single'
    str2 = "double"
    print(str1)
    print(str2)

def Indexing():
    str1 = "I'm Sohaib"
    print(str1[0]) # I
    print(str1[-1]) # b (first char form end)

def slicing():
    str1 = "I'm Sohaib"
    print(str1[4:]) # str[3] to str[end]
    print(str1[4:7]) # str[4] to str[7]
    print(str1[:7]) # from start to str[7]
    print(str1[:]) # from start to end
    print(str1[::1]) # from start to end (one step every time)
    print(str1[::2]) # from start to end (2 steps every time)

def string_methods():
    str1 = "I'm Sohaib"
    print(len(str1)) # len

    # strip - rstrip - lstrip
    # strip : remove spaces from left and right
    # lstrip: .... from left only
    # rstrip: .... from right only
    str2 = "           I'm strip           "
    print(str2.strip())
    print(str2.lstrip())
    print(str2.rstrip())

    str2 = "##########I'm strip 2 #############"
    print(str2.strip("#"))
    print(str2.lstrip("#"))
    print(str2.rstrip("#"))

    str2 = "#@#@#@#@I'm strip 3 #@#@#@#@#@"
    print(str2.strip("#@"))

    # title()
    str2 = "all text here is lower case"
    print(str2.title()) # convert me to tile format

    # capitalize()
    str2 = "all text here is lower case"
    print(str2.capitalize())

    # zfill()
    c, d, e = "1", "11", "111"
    print(c.zfill(3))
    print(d.zfill(3))
    print(e.zfill(3))

    # upper()
    name = "sohaib"
    print(name.upper())
    name = "SOHAIB"
    print(name.lower())

    ### split () - rsplit() - lsplit()
    str1 = "I love python and sohaib"
    print(str1.split()) # split by spaces

    str1 = "I-love-python-and-sohaib"
    print(str1.split("-")) # split by -
    print(str1.split("-", 2)) # split by - and max = 2
    print(str1.rsplit("-", 2)) # split by - and max = 2 - form right

    # center()
    e = "sohaib"
    print(e.center(40, "$"))

    # count
    e = "I love sohiab sohaib sohiab"
    print(e.count("sohaib"))
    print(e.count("sohaib", 0, 20)) # from char 0 to 20

    e = "I love sohiab sohaib sohiab"
    print(e.swapcase())

    # startswith()
    e = "I love sohiab sohaib sohiab"
    print(e.startswith("I"))
    print(e.startswith("I", 2, 30))

    print(e.endswith("b"))

    # index(subString [, Start, End])
    e = "I love sohiab sohaib sohiab"
    #           ^      ^
    print(e.index("s")) # 7
    print(e.index("s", 8, 20)) # 14
    #print(e.index("z")) # will panic your code

    # find(subString [, Start, End])
    print("====== find")
    print(e.find("z")) # -1
    print(e.find("s")) # 7

    # ljust() - rjust()
    e = "love"
    print(e.rjust(20)) # fill 20 char with spaces
    print(e.rjust(20, "%")) # fill 20 char with spaces

    # expandtabs()

    # istitle()
    # isspace()
    # islower()
    # isupper()
    # isidentifier()


    # isalpha()
    # isalnum()

    # replace(old, value, new value, count)
    # join()
    myList = ["sohiab", "mohammed", "abdelfattah"]
    print("$".join(myList))
    print(type("$".join(myList)))

    print(", ".join(myList))

    #######################################################################
    print("="* 100)

    # pop string impl ))
    s = "Sohaib"
    while s:
        print(s[-1])
        s = s[:-1]

    #######################################################################
    print("="* 100)

    s = "Sohaib" * 2
    print(s)

#######################################################################
def main():
    concat()
    single_double()
    Indexing()
    slicing()
    string_methods()

main()
