import numpy as np
import matplotlib.pyplot as plt
import math as m 
from numpy import random

#I. Introduction

#a sample test
n = 27
x = np.random.normal(13, 4.2, n)

x_mean = np.mean(x)


#EQ 2 : accuracy of mean(x) - estimated std
def var(X,n):
	variance = 0
	for i in range(n):
		variance += (X[i] - np.mean(X))**2

	return variance


def eststd(X,n): 
	sigchap = m.sqrt(var(X)/(n*(n-1)))

	return sigchap


#EQ 3 : sample average of the data set deleting the nth point
def xmean_del_i(X,n):
	x_i_mean = np.zeros(n)
	for i in range(n):
		x_i_mean[i] = (n*np.mean(X) - X[i])/(n-1)

	return x_i_mean

#EQ 4 : jackknife estimate of std
def varjack(X,n):
	variance = 0
	for i in range(n):
		variance += (xmean_del_i(X,n)[i] - np.mean(X))**2

	return variance

def jackstd(X,n):
	sigjack = m.sqrt((n-1)*varjack(X,n)/n)

	return sigjack

#EQ 6 : distribution with probability mass 1/n
def varboot(X,n):
	variance = 0
	for i in range(n):
		variance += (1/n**2)*(X[i] - np.mean(X))**2

	return variance

#EQ 7 : bootstrape estimate of std
def bootstd(X,n):
	sigboot = np.sqrt(varboot(X,n))

	return sigboot

#CROSS-VALIDATION : delete xi, predict with n-1, evaluate and average the predictions
#EQ 8 : estimate of expected sqr err of E
#E = (n+1)*eststd(x,n)**2

#_____________________________________________________________________
# 2. THE BOOTSTRAP

#sample in paper
xschool = np.array([[576,3.39],[635,3.3],[558,2.81],[578,3.03],[666,3.44],[580,3.07],[555,3],[661,3.43],[651,3.36],[605,3.13],[653,3.12],[575,2.74],[545,2.46],[572,2.88],[594,2.96]], dtype = np.float64)

#fig. 1
#plt.plot(xschool[:,0], xschool[:,1], 'ro')
#plt.show()

#pearson's corrcoeff
def pcorco(x):
	sumy = 0
	sumz = 0
	sumyz = 0
	sumyy = 0
	sumzz = 0

	sumyz = np.dot(x[:,0],x[:,1])
	sumy = np.sum(x[:,0])
	sumz = np.sum(x[:,1])
	sumyy = np.dot(x[:,0],x[:,0])
	sumzz = np.dot(x[:,1],x[:,1])
	R = (x.shape[0]*sumyz -sumz*sumy)/ np.sqrt((x.shape[0]*sumyy - sumy**2)*(x.shape[0]*sumzz-sumz**2))
	return R

#Empirical distribution function
def massn(x): return x/x.shape[0]

#bootstrap sample
def bootsampling(x):
	xnew = x
	maxval = int(x.shape[0]/3)
	a = 0
	b = 0
	while b < x.shape[0]:
		a = random.randint(0,maxval)
		xnew[b:b+a] = xnew[b]
		b += a+1

	return xnew

#bootstrap estimate of sigma(F)
def sigbootstrap(x, B):

	bootrep = np.zeros(B)
	for i in range(B):
		bootrep[i] = pcorco(bootsampling(massn(x)))

	#EQ 11
	sigbootchap = np.sqrt(np.sum((bootrep - np.mean(bootrep))**2)/(B-1))

	return(sigbootchap)

def signorm(x):
	sign = (1-pcorco(x)**2)/np.sqrt(x.shape[0]-3)
	return sign

#print(sigbootstrap(xschool, 1000))
#print(sign(xschool))
#plt.hist(bootrep-meanbootrep)
#plt.show()

#_____________________________________________________________________
# 3. THE JACKKNIFE

def deli(x,a):
	xnew = np.zeros(shape = x.shape[:])
	for j in range(x.shape[0]):
		if j!=a:
			xnew[j,:] = x[j,:]
	xnew = np.delete(xnew,a,axis = 0)
	return xnew

def sigjackknife(x):
	n = x.shape[0]
	stat = np.zeros(n)

	for i in range(n):
		stat[i] = pcorco(deli(x,i))

	meanstat = stat.mean()

	sig = np.sqrt((n-1)*np.sum((stat-meanstat)**2)/n)
	return sig

#print(sigjackknife(xschool))

#_____________________________________________________________________
# 7. MORE COMPLICATED DATA SETS
#new data sets
B = 100
F = random.uniform(size=6)
G = random.uniform(size=9)

def twosamples(X,Y):
	newF = bootsampling(massn(X))
	newG = bootsampling(massn(Y))

	theta = []
	for j in range(Y.shape[0]):
		for i in range(X.shape[0]):
				theta.append(newG[j] - newF[i])

	thetastar = np.median(theta)
	return thetastar

def sigbootstrap2samples(X, Y, B):

	bootrep2 = np.zeros(B)
	for i in range(B):
		bootrep2[i] = twosamples(X,Y)

	#EQ 11
	sigbootchap2 = np.sqrt(np.sum((bootrep2 - np.mean(bootrep2))**2)/(B-1))

	return(sigbootchap2)


print(sigbootstrap2samples(F,G,B))
#Hodges_Lehmann shift estimate

#_____________________________________________________________________
# 8. CROSS-VALIDATION ?