t=int(input())
d={}
for i in range(1,t+1):
    lst=[]
    m=input("enter range")
    n=(m.split())
    q,l=int(n[0]),int(n[1])
    lst.append(q)
    lst.append(l)
    d[i]=lst
for i in range(1,t+1):
    print("\n")
    for num in range(d[i][0],d[i][1]):
        if (num>1):
            isDivisible=False
            for j in range(2,num):
                if(num%j==0):
                    isDivisible=True
                    break
            if not isDivisible:
                print(num)
