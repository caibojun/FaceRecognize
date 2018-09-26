# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 09:25:10 2018

@author: Administrator
"""

#image capture
#enter 'c' the program would shot
#enter 's' camera will shutdown
import cv2 
cap = cv2.VideoCapture(0) 
cap.set(480,480)
i=0
face_cascade = cv2.CascadeClassifier(r'./haarcascade_frontalface_default.xml')
while(1): # get a frame 
    ret, frame = cap.read() # show a frame 
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,scaleFactor=1.15,minNeighbors=5,minSize=(5,5))
    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+w),(0,255,0),2)
    cv2.imshow("capture", frame) 
    if cv2.waitKey(1) & 0xFF == ord('c'): 
        cv2.imwrite("./image/"+str(i)+".jpeg", frame)
        i+=1
    elif cv2.waitKey(1) & 0xFF == ord('s'):
        break
cap.release() 
cv2.destroyAllWindows()