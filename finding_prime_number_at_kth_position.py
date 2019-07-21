#finding the prime number at the kth position
def kprime(n):
    counter=2
    rage=num
    nthlist=[]
    while(rage>0):
        isDivisible=False
        for i in range(2,counter):
            if(counter%i==0 and counter !=2):
                isDivisible=True
                break
        if not isDivisible:
            rage=rage-1
            nthlist.append(counter)
        counter=counter+1
    return nthlist[-1]


if __name__=="__main__":
    t=int(input())
    lst=[]
    for i in range(1,t+1):
        lst.append(int(input()))
    #print(lst)
    for num in lst:
        result=kprime(num)
        print(result)
