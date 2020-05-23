import itertools
m=0
for i in itertools.count(1):
	count=0
  for j in range(1,i+1):
		if i%j==0:
			count+=1
			if count==2:
				m+=1
        print(m," ",i)
        if m==10001:
					break
