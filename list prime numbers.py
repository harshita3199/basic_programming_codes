#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#to list all prime no between range
index1=int(input("Enter the lower range"))
index2=int(input("Enter the upper range"))

print("prime numbers between {0} and{1} are".format(index1,index2))

for num in range(index1,index2+1):
    if (num>1):
        isDivisible=False
        for i in range(2,num):
            if(num%i==0):
                isDivisible=True
        if not isDivisible:
            print(num)

