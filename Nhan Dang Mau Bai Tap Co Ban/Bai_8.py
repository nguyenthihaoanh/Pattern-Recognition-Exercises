import numpy as np 
import matplotlib.pyplot as plt 
import random
import math
import sklearn 
from sklearn.model_selection import train_test_split
data_1 = []
with open("class1.txt",'r')as f:
    for line in f:
        data_1=np.array(f.read().split(),np.float)
    x_train_1,x_test_1=train_test_split(data_1,test_size=0.5)
print(data_1)
with open("class2.txt",'r')as f:
    data_2=np.array(f.read().split(),np.float)
    x_train_2,x_test_2=train_test_split(data_2,test_size=0.5)

print(x_test_1)
#print('Mean va variance cua class1:'+np.str(np.mean(data_1)+' ')       