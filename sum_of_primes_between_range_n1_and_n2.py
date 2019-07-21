#sum of prime numbers between range n1 and n2
def pn(n,m):
    sum=0
    for num in range(n,m+1):
        isDivisible=False
        if (num>0):
            for i in range(2,num):
                if(num%i==0):
                    isDivisible=True
                    break
            if not isDivisible:
                #print(num)
                sum+=num
    return sum

def npn(n,m):
    sum=0
    for num in range(n,m+1):
        isDivisible=False
        if (num>0):
            for i in range(2,num):
                if(num%i==0):
                    isDivisible=True
                    break
            if not isDivisible:
                #print(num)
                sum+=num
    return sum
if __name__=="__main__":
    n1=int(input())
    n2=int(input())
    if (n1<n2):
        result=pn(n1,n2)
        print (result)
    else:
        result=npn(n2,n1)
        print (result)
