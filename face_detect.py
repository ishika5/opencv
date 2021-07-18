import cv2 

img = cv2.imread('lady.jpg')

cv2.imshow('lady',img)
gray =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray lady',gray)

cascade = cv2.CascadeClassifier('face.xml')

faces_react = cascade.detectMultiScale(gray , scaleFactor=1.1 , minNeighbors = 3)
print(f'Number of faces ={len( faces_react)}')

for (x,y,w,h) in faces_react:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),thickness =2) 

cv2.imshow('Detected faces' , img)
       
cv2.waitKey(0)

