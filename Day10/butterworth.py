import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
T=0.1 #sec
w_p=0.35*np.pi
w_s=0.7*np.pi
del_p=0.6
del_s=0.1
x=np.tan(w_p/2)
omega_p=(2*x)/T
y=np.tan(w_s/2)
omega_s=(2*y)/T
print "omega_p=",omega_p
print "omega_s=",omega_s
x1=(del_s**-2)-1
x2=(del_p**-2)-1
x3=np.sqrt(x1/x2)
x4=np.log(x3)
x5=np.log(omega_s/omega_p)
x6=x4/x5
x7=np.abs(x6)
N=np.ceil(x7)
print "original order=",x7
print "order=",N
y1=x1**(0.5/N)
omega_c=omega_s/y1
print "omega_c=",omega_c
k=N/2
p1=(2*k-1)*0.25
b_k=2*np.sin(p1*np.pi)
print b_k
j=cm.sqrt(-1)
#w=np.arange(0,np.pi,0.01)
w=np.arange(-np.pi,np.pi,0.01)
z=np.exp(j*w)
s=(2*(z-1))/((z+1)*T)
print s
p2=((s**2)+(b_k*s*omega_c)+(omega_c**2))
h_z=omega_c**2/p2
plt.plot(w,np.abs(h_z))
plt.show()
