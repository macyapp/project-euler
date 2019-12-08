import math
i=0
j=0
max=0
n=600851475143
print("The prime factors are:")
for i in range(1,int(math.sqrt(n)+1)):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2 and n%i==0:
        print(i,end=' ') #This line lists the factors
print("\nThe Largest Prime factor is ",max)
