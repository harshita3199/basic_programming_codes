#to find out largest prime number below 1 million i.e.,10,00,000
def genPrime(n):
    suum=0
    ans=0
    lst=[]
    for num in range(2,n+1):
        if (num>0):
            isDivisible=False
            for i in range(2,num):
                if(num%i==0):
                    isDivisible=True
                    break
            if not isDivisible:
                suum +=num
                if (suum<n):
                    ans=isPrime(suum)
                    if (ans==1):
                        lst.append(suum)
    #print(lst) 
    return lst

def isPrime(no):
    isDivisible=False
    for i in range(2,no):
        if (no%i==0):
            isDivisible=True
            break
    if not isDivisible:
        return 1
       
if __name__=="__main__":
    print("generating prime numbers....")
    n=int(input())
    result=genPrime(n)
    final=result[-1]
    if not result:
        print("1") 
    else:
        print("({})MOD10007".format(final))
   
