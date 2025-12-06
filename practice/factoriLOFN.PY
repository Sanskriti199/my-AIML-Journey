def cal_fact(n):
    fac=1
    for i in range(1,n+1):
        fac*=i
    return fac

n=int(input("enter n:"))
print(cal_fact(n))

