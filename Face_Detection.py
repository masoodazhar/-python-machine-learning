
#   Face Detection

#   Importing face detector libraray and openCV
#   bleedfacedetector library have to install by using the pip command
# " pip install bleedfacedetector "
#   and cv2 
# " pip install opencv-python "
#   for latest version


import bleedfacedetector as faceDetect
import cv2


cap = cv2.VideoCapture(0)  # connecting the camera ans set it to the Cap variable

while(cap.isOpened()): # loop is will be continue until the cap is opened
    
    _, frame = cap.read() # reading the cap variable which we connected before starting the while loop 
    
    faces = faceDetect.ssd_detect(frame,conf=0.3) 

    for (x,y,w,h,) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.putText(frame,'Face Detected',(x,y+h+15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 2, cv2.LINE_AA)
    
    cv2.imshow("window", frame)
    
    if cv2.waitKey(1) == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()