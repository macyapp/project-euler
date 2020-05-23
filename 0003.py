import math
max=None
n=600851475143
print("The prime factors are:")
for i in range(1,int(math.sqrt(n)+1)):
	count=0
	for j in range(1,i+1):
		if i%j==0:
			count+=1
			if count>2:
				break
	if count==2 and n%i==0:
		if max is None or i>max:
			max=i
		print(i,end=' ') #This line lists the factors
print("\nThe Largest Prime factor is",max)
