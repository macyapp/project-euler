i=0
j=0
n=2000000
sum=0
print("The sum is:")
for i in range(1,n+1):
    count=0            #No. of factors for the number 'i'
    for j in range(1,i+1):
        if i%j==0:
            count+=1
        if count>2:    #This line breaks the loop if there are more than 2 factors for a number
            break
    if count==2:
        sum+=i
        print(i," ",sum)
