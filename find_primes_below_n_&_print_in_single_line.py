#print all primes in single line below N
def genPrime(n):
    lst=[]
    for num in range(2,n+1):
        isDivisible=False
        if(num>0):
            for i in range(2,num):
                if(num%i==0):
                    isDivisible=True
                    break
            if not isDivisible:
                lst.append(num)
    return lst

if __name__=="__main__":
    N=int(input())
    result=genPrime(N)
    for i in result:
        print(i,end=" ")
