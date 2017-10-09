import matplotlib.pyplot as plt
import numpy as np
import math
from scipy import stats

inputdata = np.loadtxt("Pendulum_data1.txt")
data = np.transpose(inputdata)
colors = {20:'purple',40:'g',60:'r',80:'blue'}

#including all data for mass 1
length = data[0]
mass = data[1]
angle = data[2]
period = data[3]
#regular length vs. period
plt.figure(1)
for degree in [20,40,60,80]:
    #including only data where angle = 20
    fMatch = np.where(data[2] == degree)
    length = data[0][fMatch]
    period = data[3][fMatch]
    #regular length vs. period
    plt.errorbar(length, period, fmt = 'o', color=colors[degree], label=degree)
plt.xlabel("Length [cm]")
plt.ylabel("Period [s]")
plt.legend(numpoints = 1)
plt.title("Length vs. Period")
plt.show()