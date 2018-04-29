
# coding: utf-8

# In[4]:

#!/bin/python3

import sys


N = int(input().strip())
if (N%2!=0 or (N%2==0 and 6<=N<=20)):
    print ("Weird")
elif ((N%2==0 and 2<=N<=5) or (N%2==0 and N>20)):
    print ("Not Weird")
else:
    pass



