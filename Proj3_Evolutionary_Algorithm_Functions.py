# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 10:08:31 2019

@author: emyli 
Received help from (TA) Burhan Ul Haq for method toBinary and toDecimal
"""
import math
import numpy as np
def toBinary(decimal): #Recieved help from TA on this method
     res = math.modf(decimal)
     first = str(bin(int(res[1]))) # part before decimal
     first = first[2:]
     dec = res[0] # part after decimal
     strDec = ""
     while dec != 0.0:
         mul = dec * 2
         if mul >= 1.0:
             strDec += "1"
         else:
             strDec += "0"
         dec = math.modf(mul)[0]

     final =  first
     final += "."
     if not strDec:
         strDec += "0"
     final += strDec
     return final

def toDecimal(binaryStr): #Recieved help from TA on this method
    s = binaryStr.split(".")
    first = int(s[0], 2) # 100
    second = s[1] # 01
    num = 0
    power = -1
    for x in second:
        if x != "0":
            num += float(x) * 2 ** power
        power *= 2

    final = first + num
    return final

def largeOut(normOut,n):
    max_list = []
    yikes = list(normOut)
    for i in range(n):
        maximum = yikes[0]
        index = 0
        for j in range(len(yikes)):
            if maximum < yikes[j]:
                maximum = yikes[j]
                index = j
        max_list.append(maximum)
        yikes[index] = 0.0
    return max_list

def mutation(anArr):
    ugh = True
    ranInd= np.random.randint(0,(len(anArr))) #ranInd will be a number from 0 - length of anArr
    ranStr = anArr[ranInd] # ranStr is the string from the ran index
    ranChar = list(ranStr) # place string into a list
    ranCIn =  np.random.randint(0,(len(ranStr))) # get a ran num from the length of string
    while ugh:
        if ranChar[ranCIn] != '.':
            ugh = False
            if ranChar[ranCIn] != '0':
                ranChar[ranCIn] = '0'
                bigOofs = "".join(ranChar)
                if 3.0 <= toDecimal(bigOofs) <= 10.0:
                    ugh = False
                    anArr[ranInd] = bigOofs
                else: 
                    ranCIn  =  np.random.randint(0,(len(ranStr)))
            else: 
                ranChar[ranCIn] = '1'
                bigOofs = "".join(ranChar)
                if 3.0 <= toDecimal(bigOofs) <= 10.0:
                    ugh = False
                    anArr[ranInd] = bigOofs
                else:
                    ranCIn  =  np.random.randint(0,(len(ranStr)))
        else:
            ranCIn  =  np.random.randint(0,(len(ranStr)))

def crossOver(arX):
    ugh = True
    crossX = []
    section = np.random.randint(0,(len(arX)))
    while ugh:
        for i in range(len(arX)):
            if i == len(arX)-1:
                str = arX[0]
                str2 = arX[i]
                strsplit1, strsplit2 = str[:section],str2[section:]
                str3 = strsplit1+strsplit2
                if "." in str3:
                    if 3.0 <= toDecimal(str3) <= 10.0:
                        ugh = False
                        crossX.append(str3)
                else:
                    crossOver(arX)
            else:
                str = arX[i]
                str2 = arX[i+1]
                strsplit1, strsplit2 = str[:section],str2[section:]
                str3 = strsplit1+strsplit2
                if "." in str3:
                    if 3.0 <= toDecimal(str3) <= 10.0:
                        ugh = False
                        crossX.append(str3)
                else:
                    crossOver(arX)
    return crossX

def crossOver2(arY):
    ugh = True
    crossY = []
    section = np.random.randint(0,(len(arY)))
    while ugh:
        for i in range(len(arY)):
            if i == len(arY)-1:
                str = arY[0]
                str2 = arY[i]
                strsplit1, strsplit2 = str[:section],str2[section:]
                str3 = strsplit1+strsplit2
                if "." in str3:
                    if 4.0 <= toDecimal(str3) <= 8.0:
                        ugh = False
                        crossY.append(str3)
                    else:
                        crossOver2(arY)
            else:
                str = arY[i]
                str2 = arY[i+1]
                strsplit1, strsplit2 = str[:section],str2[section:]
                str3 = strsplit1+strsplit2
                if "." in str3:
                    if 4.0 <= toDecimal(str3) <= 8.0:
                        ugh = False
                        crossY.append(str3)
                    else:
                        crossOver2(arY)
    return crossY