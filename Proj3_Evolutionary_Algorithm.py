# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 11:05:00 2019

@author: emyli
"""
import math
import numpy as np
import Proj3_Evolutionary_Algorithm_Functions as fun
#arrays for our data/chromosomes
averageY, averageX,outputDec, outputBin, holdX, holdY, binY, binX, normOut, normY, normX, maxOut, yas, maxY, maxX = [],[],[],[],[],[],[],[],[],[],[],[],[],[],[]

#create the x & y chromosomes
for i in range(100):
  x = np.random.uniform(3,10)
  y = np.random.uniform(4,8)
  holdY.append(y)
  holdX.append(x)
  outputs = round(math.sin(math.radians(math.pi*10*x+(10/(1+y**2)))) + math.log((x**2)+(y**2)),2)
  outputDec.append(outputs)

j = 0
for j in range(10):
    #create needed lists
    popXDec, popYDec, newPopX, newPopY= [],[],[],[]

    #binary for out, x and y
    for i in range(len(outputDec)):
        outputBin.append(fun.toBinary(outputDec[i]))    
        binX.append(fun.toBinary(holdX[i]))
        binY.append(fun.toBinary(holdY[i]))
        
    #back to dec for outputs
    for i in range(len(outputBin)):
        normOut.append(fun.toDecimal(outputBin[i]))
        
    # do selection
    maxOut = fun.largeOut(normOut,50)
        
    # find the index where the largest numbers are and their respective x and y
    for i in range(len(maxOut)):
        yas.append(normOut.index(maxOut[i]))
        maxX.append(binX[yas[i]])
        maxY.append(binY[yas[i]])
            
    # do crossover on binary of max numbers x & y    
    # create new population of X and Y 
    newPopX.extend(maxX)
    newPopX.extend(fun.crossOver(maxX))
    newPopY.extend(maxY)
    newPopY.extend(fun.crossOver2(maxY))

    # do mutation on one of the parents from x
    fun.mutation(newPopX) 
    
    #turn new populations to decimal
    for i in range(len(newPopX)):
        popXDec.append(fun.toDecimal(newPopX[i]))
        popYDec.append(fun.toDecimal(newPopY[i]))
        
    # add the average of the new population
    average = sum(outputDec)/(len(outputDec))
    averageX.append(average)
    if j == 9:
        indexOf = outputDec.index(max(outputDec))
        print "Maximum output of the function:", max(outputDec)
        print "Maximum x is:",holdX[indexOf]
        print "Maximum y is", holdY[indexOf]
        print "Number of Generations: 10"
        print "Population size: 100"
        print "Mutation probability: 1%"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #create a new generation
    holdY, holdX,outputDec = [],[],[]
    for i in range(len(popXDec)):
        x = popXDec[i]
        y = popYDec[i]
        holdY.append(y)
        holdX.append(x)
        outputs = round(math.sin(math.radians(math.pi*10*x+(10/(1+y**2)))) + math.log((x**2)+(y**2)),2)
        outputDec.append(outputs)
    outputBin, binY, binX, normOut, maxOut, yas, maxY, maxX = [],[],[],[],[],[],[],[]

# plot
import matplotlib.pyplot as plt
plt.plot (averageX)
plt.xlabel("Number of Generations",fontsize=14)
plt.ylabel("Average", fontsize = 14)
plt.title("Evolution Of The Average from F(x,y)", fontsize = 15)
plt.grid()
plt.show()

    