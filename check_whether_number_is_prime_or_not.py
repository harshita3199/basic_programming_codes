#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#to check whether it is prime no or not
num= int(input("Enter the number:"))

isDivisible =False

i=2
while i<num:
    if num%i==0:
        isDivisible=True
        print("{} is divisible by {}".format(num,i))
        break
    i+=1
if isDivisible:
    print("{} is NOT a prime number".format(num))
else:
    print("{} is a prime number".format(num))

