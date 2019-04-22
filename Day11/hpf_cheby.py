import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
T=0.1 #sec
w_p=0.7*np.pi
w_s=0.35*np.pi
del_p=0.6
del_s=0.1
x=np.tan(w_p/2)
omega_p=(2*x)/T
y=np.tan(w_s/2)
omega_s=(2*y)/T
print "omega_p=",omega_p
print "omega_s=",omega_s
om_pbar=1
om_sbar=omega_p/omega_s
x1=(del_s**-2)-1
x2=(del_p**-2)-1
x3=np.sqrt(x1/x2)
x4=np.arccosh(x3)
x5=np.arccosh(om_sbar/om_pbar)
x6=x4/x5
x7=np.abs(x6)
N=np.ceil(x7)
print "original order=",x7
print "order=",N
eps=np.sqrt(x2)
print "eps=",eps
n1=(eps**-2)+1
n2=np.sqrt(n1)+eps**-1
n3=1/N
n4=n2**n3
n5=n2**-n3
Y_n=0.5*(n4-n5)
print "Y_n=",Y_n
k=N/2
p1=(2*k-1)*0.25
p2=(np.cos(p1*np.pi))**2
c_k=Y_n**2+p2
print "c_k=",c_k
b_k=2*Y_n*np.sin(p1*np.pi)
print "b_k=",b_k
j=cm.sqrt(-1)
w=np.arange(0,np.pi,0.01)
#w=np.arange(-np.pi,np.pi,0.01)
z=np.exp(j*w)
s=(2*(z-1))/((z+1)*T)
s_bar=omega_p/s
#print "s_bar=",s_bar
h1=((s_bar**2)+(b_k*s_bar*om_pbar)+(om_pbar**2)*c_k)
h_z=del_p*(om_pbar**N)*c_k/h1
plt.plot(w,np.abs(h_z))
plt.show()

