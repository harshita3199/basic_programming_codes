#nth prime number
def genPrime(nthNum):
    rage = nthNum
    counter = 2
    nthList = []
    while rage > 0:
        isDivisible = False
        for i in range(2,counter):
            if(counter % i == 0 and counter != 2):
                isDivisible = True
                break
                # print("Not a Prime")
        if not isDivisible:
            rage = rage - 1
            # print(rage)
            nthList.append(counter)
        counter = counter + 1
    return nthList[-1]

if __name__ == "__main__":
    t=int(input())
    lst=[]
    count=0
    for i in range(1,t+1):
        lst.append(int(input("enter {} number".format(i))))
    print(lst)
    for nthNum in lst:
        result = genPrime(nthNum)
        print("Result",result)
