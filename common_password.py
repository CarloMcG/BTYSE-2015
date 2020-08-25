# checks an example password against a list of the 10,000 most common passwords
string = input("password: ")

def check():
    datafile = open('passwords.txt')
    found = False
    for line in datafile:
        if string in line :
            found = True
            break
    return found
found = check()
if found:
    print("This password is common")
else:
    print("This password is uncommon")