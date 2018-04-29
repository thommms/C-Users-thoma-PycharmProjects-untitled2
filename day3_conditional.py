
# coding: utf-8

# A game that poses condition on a user
'''If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird'''


N = int(input().strip())
if (N%2!=0 or (N%2==0 and 6<=N<=20)):
    print ("Weird")
elif ((N%2==0 and 2<=N<=5) or (N%2==0 and N>20)):
    print ("Not Weird")
else:
    pass



