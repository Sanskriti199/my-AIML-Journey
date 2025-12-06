word="artificial"

count=0

for ch in word:
    if(ch=='i' or ch=='e' or ch=='a' or ch=='o' or ch=='u'):
        count+=1

print("ans:", count)