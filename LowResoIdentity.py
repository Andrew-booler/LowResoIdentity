import cv2
import numpy as num
from compiler.ast import flatten
import matplotlib.mlab as mlab    
import matplotlib.pyplot as plt    
dic=num.empty([0,0])
# input original images
for k in range(1,16):
    print(k)    #print image number
    img=cv2.imread('F:/mine/FaceImg/'+str(k)+'/s1.bmp')
    #  transform into gray image
    grayimg=num.empty([img.shape[0],img.shape[1]],img.dtype)
    for i in range(0,img.shape[0]):  
        for j in range(0,img.shape[1]):  
            grayimg[i][j] = img[i][j][0]
    # linearize and collect
    if k==1:
        dic=[grayimg.flatten()]
    else:
        dic.append(grayimg.flatten())
dic=num.matrix(num.stack(dic))
#input the image to be identified
img=cv2.imread('F:/mine/FaceImg/1/s1.bmp')
# transform into a gray one
grayimg=num.empty([img.shape[0],img.shape[1]],img.dtype)
for i in range(0,img.shape[0]):  
        for j in range(0,img.shape[1]):  
            grayimg[i][j] = img[i][j][0]
# identify
res=grayimg.flatten()*dic.I
# result
print res.getA1()
label=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

fig=plt.figure()
plt.bar(label,res.getA1(),0.4,color="green")
plt.xlabel("faces")
plt.ylabel("similarity")
plt.show()
