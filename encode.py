# import os


def convert(s):
    # initialization of string to "" 
    new = ""

    # traverse in the string  
    for x in s:
        new += x

        # return string
    return new


def encode(text):
    text = text
    size = len(text)
    for i in range(size):
        pass


def intostring(test):
    # initialize array
    test = test
    length = len(test)
    for i in range(length):
        if i == 0:
            savelist = [test[i]]
        else:

            savelist.append(test[i])
    return savelist

    # "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",


newlist = []
newlist2 = []


def convert_to_ceaser(character_1):
    for x in range(len(normal)):
        if character_1 == normal[x]:
            newlist.append(x)
            #print(normal[x])
        else:
            pass


def ceaser2():
    for x in range(len(newlist)):
        newlist2.append(ceasear[newlist[x]])


def passvalues():
    for x in range(len(concatinate)):
        convert_to_ceaser(concatinate[x])


normal = ["A", "B,", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
          "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
          "s", "t", "u", "v", "w", "x", "y", "z", ]
ceasear = ["X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
           "T", "U", "V", "W", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
           "p", "q", "r", "s", "t", "u", "v", "w"]

# print('press 1 to use md5')
code = (input("enter key to be encoded : "))
# julian script
# print(code.index(0))
#size = (len(code))
#print(code.split())
concatinate = (intostring(code))
passvalues()
ceaser2()


#print(concatinate)
print(convert(concatinate))
print(convert(newlist2))
