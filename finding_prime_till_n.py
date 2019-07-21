#finding the prime number till n
def listprime(num):
    lst=[]
    print(num)
    for n in range(2,num+1):
        if(n>0):
            isDivisible=False
            for i in range(2,n):
                if(n%i==0):
                    isDivisible=True
                    break
            if not isDivisible:
                #print(n)
                lst.append(n)
    return lst
if __name__ == "__main__":
    n=int(input())
    result=listprime(n)
    #print(result)
    for out in result:
        print(out, end=" ")
    
