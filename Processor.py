#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import os

inputFile = r"N:\SHC\2_Projects\048_LandsatSetup\LandSat_Sig_Processor\input_0.txt"

listClasses = []
listIndexPts = []

class L8Stats:
    def __init__(self,nameClass):
        self.className = nameClass
        self.listHeader = ["CoastalAerosol","Blue","Green",
                      "Red","NearInfrared","ShortWaveInfrared_1",
                      "ShortWaveInfrared_2","Cirrus"]
        self.dictHeader = {1:"CoastalAerosol",2:"Blue",3:"Green",
                      4:"Red",5:"NearInfrared",6:"ShortWaveInfrared_1",
                      7:"ShortWaveInfrared_2",8:"Cirrus"}
        #  (min, Mean, max)
        self.band1 = ()
        self.band2 = ()
        self.band3 = ()
        self.band4 = ()
        self.band5 = ()
        self.band6 = ()
        self.band7 = ()
        self.band8 = ()
    def __name__(self):
        self.className
        
        
fo = open(inputFile,"r")
data = fo.readlines()
k = 0

#scan for classes
for lines in data:
    if lines[0:5] == 'Class':
        #print k
        listIndexPts.append(k)
    k = k + 1

listClasses = []
for lines in listIndexPts:
    thisClass = L8Stats( data[lines].rstrip() )  #class name
    #print "|"+data[lines]+"|"  
    #print data[lines+1].rstrip().split('\t')   #   header row
    mins =  data[lines+2].rstrip().split('\t')   #   mins
    #print mins
    maxes =  data[lines+3].rstrip().split('\t')   #   maxes
    #print maxes
    means = data[lines+4].rstrip().split('\t')   #   mean
    #print means
    for i in range(1,9):
        string = 'thisClass.band'+str(i)+"  = ( mins["+str(i)+"],means["+str(i)+"],maxes["+str(i)+"])"
        #print string
        exec string
        #thisClass.band1 = ( mins[1],means[1],maxes[1])
        string = 'thisClass.band'+str(i)
        #print eval(string)
    listClasses.append(thisClass)

x = np.arange(0,10,1)
print x

for items in range(10):
    thisMin = 0

def DefineBandClass(inputClass):
    y = []
    y_t = []
    y_b = []
    y_r = []
    for items in x:  # for each band
        string = 'listClasses['+str(inputClass)+'].band'+str(items)
        print string
        try:
            print eval(string)
            thisTuple = eval(string)
            y.append(float( thisTuple[1] ) )
            y_b.append(float( thisTuple[0] ) )
            y_t.append(float( thisTuple[2] ) )
            y_r.append(float( thisTuple[2] ) - float( thisTuple[0]) )
        except:
            y.append(0)
            y_b.append(0)
            y_t.append(0)
            y_r.append(0)
    print y#,y_b,y_t
    return (y,y_b,y_t,y_r)


(y,y_b,y_t,y_r) = DefineBandClass(0)
(y1,y_b1,y_t1,y_r1) = DefineBandClass(1)
(y2,y_b2,y_t2,y_r2) = DefineBandClass(2)

npy = np.asarray(y)
npyr = np.asarray(y_r)
print x,npy

plt.figure()
plt.errorbar(x, npy, xerr=0., yerr=npyr, color="blue")

npy = np.asarray(y1)
npyr = np.asarray(y_r1)
plt.errorbar(x, npy, xerr=0., yerr=npyr, color="red")

npy = np.asarray(y2)
npyr = np.asarray(y_r2)
plt.errorbar(x, npy, xerr=0., yerr=npyr, color="purple")

plt.show()


    
