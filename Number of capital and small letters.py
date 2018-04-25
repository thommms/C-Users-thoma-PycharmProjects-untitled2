#Number of capital and small letters in a string
i=0
j=0
string=input("enter a string: ")
for letter in string:
    if letter.isupper():
        i=i+1
    elif letter.islower():
        j=j+1
    else:
        pass
print ("the number of capital letters:", i)
print ("the number of small letters:", j)