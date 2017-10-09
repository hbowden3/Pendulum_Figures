import matplotlib.pyplot as plt
import numpy as np
import math
from scipy import stats

inputdata = np.loadtxt("Pendulum_data1.txt")
data = np.transpose(inputdata)

#including all data for mass 1
length = data[0]
mass = data[1]
angle = data[2]
period = data[3]
#regular length vs. period
plt.figure(1)
plt.plot(length, period, 'ro')
plt.xlabel("Length [cm]")
plt.ylabel("Period [s]")
plt.title("Length vs. Period")
#sqrt of length vs. period
plt.figure(2)
plt.plot(np.sqrt(length), period, 'ro')
plt.xlabel("Length [cm]")
plt.ylabel("Period [s]")
plt.title("Length vs. Period")

#including only data where angle = 20
fMatch = np.where(data[2] == 20)
length = data[0][fMatch]
period = data[3][fMatch]
#regular length vs. period
plt.figure(3)
plt.plot(length, period, 'ro')
plt.xlabel("Length [cm]")
plt.ylabel("Period [s]")
plt.title("Length vs. Period")
#sqrt of length vs. period
plt.figure(4)
plt.plot(np.sqrt(length), period, 'ro')
plt.xlabel("Length [cm]")
plt.ylabel("Period [s]")
plt.title("Length vs. Period")

#including only data where angle = 80
fMatch = np.where(data[2] == 80)
length = data[0][fMatch]
period = data[3][fMatch]
#regular length vs. period
plt.figure(5)
plt.plot(length, period, 'ro')
plt.xlabel("Length [cm]")
plt.ylabel("Period [s]")
plt.title("Length vs. Period")
#sqrt of length vs. period
plt.figure(6)
plt.plot(np.sqrt(length), period, 'ro')
plt.xlabel("Length [cm]")
plt.ylabel("Period [s]")
plt.title("Length vs. Period")
plt.show()                 