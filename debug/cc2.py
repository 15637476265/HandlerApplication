#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 19:58:42 2018

@author: yongxiang
"""
import numpy as np
import cv2
fr= open("allcpp.txt","r")
ls= fr.readline()
img= []
while(ls):
    if len(ls) < 5:
        pic= int(ls)
        
        img.append(cv2.imread("/home/weldroid/Tracing/debug/mast/OL_"+str(pic)+".png"))
    else:
        u= round(float(ls.split()[0]))
        v= round(float(ls.split()[1]))
        cv2.circle(img[-1],(u,v),145,(0,0,255))
        cv2.circle(img[-1],(u,v),3,(0,255,0))
        #cir
    ls= fr.readline()
cc= 0
print(len(img))
for i in img:
    cv2.imwrite(str(cc)+"cc.png",i)
    cc+= 1
