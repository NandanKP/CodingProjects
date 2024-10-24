import matplotlib.pyplot as plt
import numpy as np
import math
from numpy.polynomial.polynomial import Polynomial

xg = np.array([1.1, 0.1, 1.4, 0.3, 0.1, 0.3, 0.6, 0.7, 0.3, 0.2, 1.4, 0.3, 0.9, 0.8, 0.6, 0.7, 0.5, 0.6, 1.0, 0.2, 0.8, 0.5, 0.5, 0.8, 0.7, 0.6, 2.4, 
               0.3, 0.6, 1.0, 0.9, 0.7, 0.8, 0.6, 0.6, 0.0, 0.1, 1.7, 0.6, 0.7, 0.4, 0.6, 0.5, 0.6, 0.9, 0.2, 0.0, 0.8, 0.1, 1.0, 0.6]) #The array of expected goals
g = np.array([1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 2, 2, 1, 1, 2, 2, 0, 1, 2, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 2, 1, 0, 1, 1, 2, 1, 1, 1, 1, 0, 0, 4, 1, 
              1, 1, 1, 1, 2, 0, 0, 0, 1, 0, 1, 1]) #The array of actual goals scored

#print(xg.size)
#print(g.size)

g_final = np.delete(g, [1, 3, 5, 6, 13, 34, 44])
#print(g_final.size)
y = g_final - xg
#print(y)

Xvar = []
for i in range(51):
    a = []
    for j in range(8):
        a.append((i ** j))
    Xvar.append(a)

x_m = []
for i in range(51):
    x_m.append(i)
x = np.array(x_m)
plt.plot(x, y)
plt.xlabel("Appearance Number")
plt.ylabel("xG - G")
plt.title("Snow Salah Verification")
plt.axhline(0, color = "black")
plt.axvline(0, color = "black")

Xvart = np.transpose(Xvar)

Xvar = (np.array(Xvar)).astype('float64')
Xvart = (np.array(Xvart)).astype('float64')

beta = np.linalg.inv(Xvart.dot(Xvar)).dot(Xvart.dot(y))  #The coefficient matrix
print(beta)

xf_m = []
for i in range(51):
    xf_m.append(i)
x_final = np.array(xf_m)

y_final = (np.array(Xvar)).dot(beta) 
plt.plot(x_final, y_final)