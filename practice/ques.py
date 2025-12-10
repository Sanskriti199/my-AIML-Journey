nums=[1,2,3,4,5,10,6,7,8,9]

print(nums)
idx=0
x=int(input("enter the number whose index you want to know: "))
for val in nums:
    if(val==x):
        print(f"{x} is found at idx= {idx}")
        break
    idx+=1