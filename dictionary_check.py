# checks a given example password against the Oxford English Dictionary

string = input("password: ")

def check():
    datafile = open('dictionary.txt')
    found = Falsefor line in datafile:
    if string in line:
        found = True
        break
    return found
found = check()
if found:
    print ("This password has been found in the Oxford English Dictionary")
    else:
        print ("This password has not been found in the Oxford English Dictionary")