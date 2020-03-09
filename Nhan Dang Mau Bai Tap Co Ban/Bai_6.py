import numpy as np 
import matplotlib.pyplot as plt
from scipy.stats import norm
def abc(data,mean,var):
    std=np.sqrt(var)
    z1=(np.min(data)-mean)/std
    z2=(np.max(data)-mean)/std
    x_all = np.arange(np.min(data),np.max(data) , 0.001) 
    y2 = norm.pdf(x_all,mean,std)
    return x_all,y2

#3a
a=[1,2,4,6,9,10,20,7]
x,y=abc(a,np.mean(a),np.var(a))
plt.subplot(4,2,1)
plt.plot(x,y)
plt.title('3a')
x,y=abc(a,2,1.5)
plt.subplot(4,2,2)
plt.plot(x,y)

#3b
b=np.arange(0,101,2)
x,y=abc(b,np.mean(b),np.var(b))
plt.subplot(4,2,3)
plt.plot(x,y)
plt.title('3b')
x,y=abc(b,2,1.5)
plt.subplot(4,2,4)
plt.plot(x,y)

#3c
c=(np.arange(1,100,2))**2
x,y=abc(c,np.mean(c),np.var(c))
plt.subplot(4,2,5)
plt.plot(x,y)
plt.title('3c')
x,y=abc(c,2,1.5)
plt.subplot(4,2,6)
plt.plot(x,y)

#3d
d=[(2,4),(3,7),(4,6),(5,5),(2,3)]
x,y=abc(d,np.mean(d),np.var(d))
plt.subplot(4,2,7)
plt.plot(x,y)
plt.title('3d')
x,y=abc(d,2,1.5)
plt.subplot(4,2,8)
plt.plot(x,y)

plt.show()
