#Function that takes in lists and prints the lists without repetition
main_list=[]
old_list=[2,3,4,5,6,6,5,4,3,4,2,1,3,4,2,1,3,4,2,2,3,4,3]
sett=set(old_list)
for number in sett:
    main_list.append(number)
print (main_list)