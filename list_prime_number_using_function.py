lst=[]
def prime_number(n,m):
    for num in range(n,m+1):
        if(num>0):
            isDivisible=False
            for i in range(2,num):
                if(num%i==0):
                    isDivisible=True
                    #print("{} is divisible by {}".format(num,i))
                    break
            if not isDivisible:
                print(num)
                lst.append(num)
    return lst

x=int(input("Enter lower range"))
y=int(input("enter upper range"))
result=prime_number(x,y)
print(result)
