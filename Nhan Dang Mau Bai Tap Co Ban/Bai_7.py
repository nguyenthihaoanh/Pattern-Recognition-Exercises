import numpy as np 
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal
from scipy.spatial import distance
x=np.linspace(-10,10,100)
y=np.linspace(-10,10,100)
X,Y=np.meshgrid(x,y)
pos=np.dstack((X,Y))
mu=np.array([1,3])
cov=np.array([2,2])
rv=multivariate_normal(mu,cov)
Z=rv.pdf(pos)
fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
ax.plot_surface(X,Y,Z)
plt.show()

a=[0,0]
b=[3,4]
c=[1,2]
iv=[(2,0),(0,2)]

print('Khoang cach:'+ np.str(distance.mahalanobis(mu,a,iv)))
print('Khoang cach:'+ np.str(distance.mahalanobis(mu,b,iv)))
print('Khoang cach:'+ np.str(distance.mahalanobis(mu,c,iv)))
