i=0
j=0
n=2000000
sum=0
print("The sum is:")
for i in range(1,n+1):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
        sum+=i
        print(sum)
