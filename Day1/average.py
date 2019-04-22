n=input("enter n=");
avg=0;
sum=0;
for i in range(1,n+1):
	sum=sum+i;
	avg=float(sum/i);
print "the average of given numbers are",avg