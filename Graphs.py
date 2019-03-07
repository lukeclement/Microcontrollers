import numpy as n
import math
import matplotlib.pyplot as plt

def errorResults(data):
    output=n.array([])
    
    for i in range (0, n.size(data, 0)):
        #Finding error on each data point using data spread
        output = n.append(output, n.std(data[i], ddof=0)) #This shouldn't be used as the number of data sets is limited
    return output

def meanResults(data):
    output=n.array([])
    
    for i in range (0, n.size(data, 0)):
        output = n.append(output, n.mean(data[i]))
    return output

def chi(fit, mapFit, x, y, yError):
    chiSq=n.sum(n.square(n.divide((y-mapFit),yError)))
    RChiSq=chiSq/(x.size - 2)
    
    xA=n.linspace(n.amin(x), n.amax(x), 1000)
    
    plt.xlabel("Distance/m")
    plt.ylabel("Time taken to travel/µs")
    #plt.plot(xA, fit-fit, label='Linear fit')
    #Dealtaf stuff
    deltaf=n.empty(yError.size)
    deltaf.fill(n.sqrt(n.sum(n.power(y-mapFit,2))/(y.size-(1%2+2)-1)))
    #plt.errorbar(x, y-mapFit, deltaf, fmt='x', label='Data')
    
    print("χ\u00B2=%5.3f" %chiSq)
    print("Reduced χ\u00B2=%2.3f" %RChiSq)
    return chiSq, RChiSq

def fitting(x, y):
    xA=n.linspace(n.amin(x), n.amax(x), 1000)
    (p, cov) = n.polyfit(x, y, 1, cov=True)
    fit=n.polyval(p, xA)
    mapFit=n.polyval(p, x)
    plt.plot(xA, fit, label='Linear Fit')
        
    return fit, mapFit, p, cov


plt.style.use('_classic_test')

rawData=n.loadtxt("data.txt")

a=rawData[:, 0]
b=rawData[:, 1]

xTrue=n.empty(6)

xTrue[0] = a[0]
xTrue[1] = a[5]
xTrue[2] = a[10]
xTrue[3] = a[15]
xTrue[4] = a[20]
xTrue[5] = a[25]

y05 = n.empty(5)
y05[0] = b[0]
y05[1] = b[1]
y05[2] = b[2]
y05[3] = b[3]
y05[4] = b[4]
y10 = n.empty(5)
y10[0] = b[5]
y10[1] = b[6]
y10[2] = b[7]
y10[3] = b[8]
y10[4] = b[9]
y15 = n.empty(5)
y15[0] = b[10]
y15[1] = b[11]
y15[2] = b[12]
y15[3] = b[13]
y15[4] = b[14]
y20 = n.empty(5)
y20[0] = b[15]
y20[1] = b[16]
y20[2] = b[17]
y20[3] = b[18]
y20[4] = b[19]
y25 = n.empty(5)
y25[0] = b[20]
y25[1] = b[21]
y25[2] = b[22]
y25[3] = b[23]
y25[4] = b[24]
y30 = n.empty(5)
y30[0] = b[25]
y30[1] = b[26]
y30[2] = b[27]
y30[3] = b[28]
y30[4] = b[29]

yTrue=n.row_stack((y05,y10,y15,y20,y25,y30))
y=meanResults(yTrue)
yErr=errorResults(yTrue)

plt.xlabel("Distance/m")
plt.ylabel("Time taken to travel/µs")
plt.errorbar(xTrue, y, yErr, fmt='x', label='Sound data')

fit, mapFit, p, cov = fitting(xTrue, y)
plt.legend(loc='best')
plt.show()
print(p)
print(cov)
chiSq, RChiSq = chi(fit, mapFit, xTrue, y, yErr)