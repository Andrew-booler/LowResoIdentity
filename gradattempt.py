import cv2
import numpy as num
import matplotlib.pyplot as plt

res=num.empty([0,0])
for k in range(1,16):
    print(k)
    img=cv2.imread('F:/mine/FaceImg/'+str(k)+'/s1.bmp')
    grayimg=num.empty([img.shape[0],img.shape[1]],img.dtype)
    for i in range(0,img.shape[0]):  
        for j in range(0,img.shape[1]):  
            grayimg[i][j] = img[i][j][0]
    tmpx=cv2.Sobel(grayimg,-1,1,0)
    tmpx=cv2.convertScaleAbs(tmpx)
    tmpy=cv2.Sobel(grayimg,-1,0,1)
    tmpy=cv2.convertScaleAbs(tmpy)
    tmp=cv2.addWeighted(tmpx,0.5,tmpy,0.5,0)
    if k==1:
        dic=[tmp]
    else:
        dic.append(tmp)
print (dic[0])
cv2.imshow('grad',dic[0])
cv2.imshow('img',cv2.imread('F:/mine/FaceImg/1/s1.bmp'))
cv2.waitKey(0)