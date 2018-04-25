#to check if a number is in a given range
start=int(input("enter the beginning of the range: "))
end=int(input("enter the end of the range:"))
number=int(input("enter the number to check: "))

if number not in range (start,end):
    print ("\n",number," not in range")
else:
    print ("\nnumber is in the range")