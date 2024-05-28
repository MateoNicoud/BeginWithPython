alphabet= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def findIndex(letter):
    return alphabet.index(letter)

def diamond(letter):
    key = findIndex(letter)
    space = 1
    for i in range(0 , key + 1):
        print(" "*(key-i), end="")
        print(alphabet[i], end ="")
        if i == 0:
            print(" "*(key-i))
        if i>0:
            print(" "*space, end="")
            print(alphabet[i], end="")
            print(" "*(key-i))
            space = space +2
    space = key
    for j in range(key-1,-1,-1):
        print(" "*(key-j), end="")
        print(alphabet[j], end ="")
        if j == 0:
            print(" "*(key-j))
        if j>0:
            print(" "*space, end="")
            print(alphabet[j], end="")
            print(" "*(key-j))
            space = space -2


diamond('d')