a=1
b=1
c=1
while a<1000 :
    b=a+1
    while b<1000 :
        c=b+1
        while c<1000 :
            if pow(a,2)+pow(b,2)==pow(c,2) and a+b+c==1000:
                print(a," ",b," ",c," ",(a+b+c))
                print(a*b*c)
            c+=1
        b+=1
    a+=1
