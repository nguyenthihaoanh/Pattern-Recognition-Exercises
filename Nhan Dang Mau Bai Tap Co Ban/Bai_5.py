import numpy as np 
import matplotlib.pyplot as plt
from scipy.stats import norm

mean=5
var=3
std=np.sqrt(var)
x1=-10
x2=10
z1=(x1-mean)/std
z2=(x2-mean)/std

x = np.arange(z1, z2, 0.001) # range of x in spec
x_all = np.arange(-10, 10, 0.001) # entire range of x, both in and out of spec

y = norm.pdf(x,mean,std)
y2 = norm.pdf(x_all,mean,std)
plt.plot(x_all,y2)
plt.title('Ham mat do Gauss bai 5')



plt.show()
