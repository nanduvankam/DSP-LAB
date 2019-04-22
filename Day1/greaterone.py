a=input("enter a=");
b=input("enter b=");
c=input("enter c=");
if ((a>b) and (a>c)):
	print a,"is Greater"
elif ((b>a) and (b>c)):
	print b,"is greater"
elif ((c>a) and (c>b)):
	print c,"is greater"
elif ((a==b) and (a>c)):
	print "a,b are greater"
elif ((b==c) and (b>a)):
	print "b,c are greater"
elif ((a==c) and (c>b)):
	print "a,c are greater"
else:
	print "all are equal"
