#fibonacci series of prime
def fs(f1,f2):
    c1=0
    c=0
    ans=isPrime(f1)
    if (ans==1):
        c1+=1
    result1=isPrime(f2)
    if result1==1:
        c1+=1
    count=0
    suum=0
    lst=[]
    while(count<20):
        f3=f1+f2
        f1=f2
        f2=f3
        result=isPrime(f3)
        if (result==1):
            c +=1
        count +=1
    return (c+c1)
        
        

def isPrime(n):
    if (n>0):
        isDivisible=False
        for i in range(2,n):
            if(n%i==0):
                isDivisible=True
                break
        if not isDivisible:
            return 1
        
            
if __name__=="__main__":
    t=int(input())
    d={}
    for i in range(1,t+1):
        lst=[]
        m=input()
        n=(m.split())
        q,l=int(n[0]),int(n[1])
        lst.append(q)
        lst.append(l)
        d[i]=lst
    #print(d)
    for i in range(1,t+1):
        result=fs(d[i][0],d[i][1])  
        print("count of {}:".format(i),result)
