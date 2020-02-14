#!/home/weldroid/anaconda3/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 18:01:04 2018

@author: yongxiang
"""
import numpy as np
#import os
import pandas as pd
import matplotlib .pyplot as plt

circleCentrePts= open("circleCentrePts.txt",'r')
cl= [[] for i in range(11)]
print(len(cl))
ls= circleCentrePts.readline()
while(ls):
    if ls[-2] == ":":
        pl= cl[int(ls[:-2])//4]
    elif ls[-2] in "0123456789":
        pl.append((int(ls.split()[0]),int(ls.split()[1]),))
    #print(ls,pl)
    ls= circleCentrePts.readline()
circleCentrePts.close()
clpd= pd.DataFrame(columns= ["u","v","nd"])
for i in range(11):
    clpdi= pd.DataFrame(cl[i],columns= ["u","v"])
    clpdi["nd"]= i
    clpd= clpd.append(clpdi)
clpd.index= list(range(len(clpd)))

clpd= clpd.sort_values("u")
uvfit= []
start= 0
lenth= len(clpd)
for i in range(lenth-1):
    if clpd.u.iloc[i+1]-clpd.u.iloc[i] > 50:
        up= clpd.iloc[start:i+1]
        start= i+1
        if len(uvfit)%2 == 0:
            uvfit.append((np.poly1d(np.polyfit(list(up.nd),list(up.u),1)),\
                          np.poly1d(np.polyfit(list(up.nd),list(up.v),1))))#.append(ps.iloc[start:].mean())
        else:
            fit1d= np.poly1d(np.polyfit(list(up.nd),list(up.v),1))
            upu= pd.DataFrame(columns= up.columns)
            upd= pd.DataFrame(columns= up.columns)
            for j in up.index:
                if up.loc[j].v < fit1d(up.loc[j].nd):
                    upu.loc[j]= up.loc[j]
                else:
                    upd.loc[j]= up.loc[j]
            uvfit.append([np.poly1d(np.polyfit(list(upu.nd),list(upu.u),1)),\
                  np.poly1d(np.polyfit(list(upu.nd),list(upu.v),1)),\
                  np.poly1d(np.polyfit(list(upd.nd),list(upd.u),1)),\
                  np.poly1d(np.polyfit(list(upd.nd),list(upd.v),1))])
        #plt.figure()
        #plt.scatter(list(up.nd),list(up.v))
up= clpd.iloc[start:]
uvfit.append((np.poly1d(np.polyfit(list(up.nd),list(up.u),1)),\
                          np.poly1d(np.polyfit(list(up.nd),list(up.v),1))))
#plt.figure()
#plt.scatter(list(up.nd),list(up.v))
uvfit[1][2],uvfit[3][0]= uvfit[3][0],uvfit[1][2]
uvfit[1][3],uvfit[3][1]= uvfit[3][1],uvfit[1][3]

print(type(uvfit[-1]))
fw= open("allcpp.txt","w")
for i in range(11):
    fw.write(str(i*4)+"\n")
    
    fw.write(str(uvfit[1][0](i)))
    fw.write(" ")
    fw.write(str(uvfit[1][1](i)))
    fw.write("\n")
    fw.write(str(uvfit[1][2](i)))
    fw.write(" ")
    fw.write(str(uvfit[1][3](i)))
    fw.write("\n")
    
    for j in range(0,5,2):
        fw.write(str(uvfit[j][0](i)))
        fw.write(" ")
        fw.write(str(uvfit[j][1](i)))
        fw.write("\n")

    fw.write(str(uvfit[3][0](i)))
    fw.write(" ")
    fw.write(str(uvfit[3][1](i)))
    fw.write("\n")
    fw.write(str(uvfit[3][2](i)))
    fw.write(" ")
    fw.write(str(uvfit[3][3](i)))
    fw.write("\n")
            
fw.close()
        
