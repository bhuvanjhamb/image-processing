#bhuvan's submission for eyantra hactober fest (image processing)

import numpy as np
import cv2

cap = cv2.VideoCapture(0)#opens the camera

    # Capture frame-by-frame
def greenCircleDetect():# to detect and draw green contour around green circle
     a=0;b=255;c=0;#describes color of contour
     lower_green = np.array([35,30,50])#HSV range for green color
     upper_green = np.array([75,255,255])
     mask = cv2.inRange(hsv, lower_green, upper_green)#creating the mask
     res = cv2.bitwise_and(frame,frame, mask= mask)
     img = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)#BGR to Gray conversion
     img = cv2.medianBlur(img,5)
     cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)#again gray to BGR conversion
     try:# to deal with the case when there are no circles so nonetype object is returned 
        circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,
                            param1=50,param2=30,minRadius=0,maxRadius=0)#finding circles using hough transform
        circles = np.uint16(np.around(circles))
        print("green circle detected")
        for i in circles[0,:]:
            # draw the outer circle
               cv2.circle(cimg,(i[0],i[1]),i[2],(a,b,c),2)
               cv2.circle(ori,(i[0],i[1]),i[2],(a,b,c),2)
            # draw the center of the circle
               cv2.circle(cimg,(i[0],i[1]),2,(a,b,c),3)
               cv2.circle(ori,(i[0],i[1]),i[2],(a,b,c),2)
     except:
        print("no green circle")
def redCircleDetect():#similar to above commented function to detect green circles
     a=0;b=0;c=255;
     lower_red = np.array([0,70,50])
     upper_red = np.array([10,255,255])
     mask = cv2.inRange(hsv, lower_red, upper_red)
     res = cv2.bitwise_and(frame,frame, mask= mask)
     img = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
     img = cv2.medianBlur(img,5)
     try:
        circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,
                            param1=50,param2=30,minRadius=0,maxRadius=0)
        circles = np.uint16(np.around(circles))
        print("red circle detected")
        for i in circles[0,:]:
            # draw the outer circle
               cv2.circle(cimg,(i[0],i[1]),i[2],(a,b,c),2)
               cv2.circle(ori,(i[0],i[1]),i[2],(a,b,c),2)
            # draw the center of the circle
               cv2.circle(cimg,(i[0],i[1]),2,(a,b,c),3)
               cv2.circle(ori,(i[0],i[1]),i[2],(a,b,c),2)
     except:
        print("no red circle")
def blueCircleDetect():#similar to above commented function to detect blue circles
    a=255;b=0;c=0;
    lower_blue = np.array([90,50,50])
    upper_blue = np.array([130,255,255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    res = cv2.bitwise_and(frame,frame, mask= mask)
    img = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
    img = cv2.medianBlur(img,5)
    cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
    try:
        circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,
                            param1=50,param2=30,minRadius=0,maxRadius=0)
        circles = np.uint16(np.around(circles))
        print("blue circle detected")
        for i in circles[0,:]:
            # draw the outer circle
               cv2.circle(cimg,(i[0],i[1]),i[2],(a,b,c),2)
               cv2.circle(ori,(i[0],i[1]),i[2],(a,b,c),2)
            # draw the center of the circle
               cv2.circle(cimg,(i[0],i[1]),2,(a,b,c),3)
               cv2.circle(ori,(i[0],i[1]),i[2],(a,b,c),2)
    except:
        print("no blue circle")
while True:
	ret, frame = cap.read()
	ori=frame#a copy of original image on which contours are drawn
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	greenCircleDetect()

	redCircleDetect()

	blueCircleDetect()


	cv2.imshow('frame', ori)

	cv2.waitKey(3)

cap.release()
cv2.destroyAllWindows()
