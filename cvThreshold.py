import cv2
import cv2.cv as cv
import numpy as np
import imutils

def nothing(x):
    pass

b=cv2.getTrackbarPos('Blur','trackbar')

img = cv2.imread('owlFiltered.jpg')
imgOrg = cv2.imread('owlFiltered.jpg')
#imgOrg=imutils.resize(imgOrg,width=432,height=324)
#img=imutils.resize(img,width=432,height=324)
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.namedWindow('trackbar')
cv2.createTrackbar('Threshold','trackbar',0,255,nothing)
cv2.createTrackbar('Kernel','trackbar',2,20,nothing)
cv2.createTrackbar('Erosion','trackbar',0,5,nothing)
cv2.createTrackbar('Dilation','trackbar',0,5,nothing)

#eroding the image


img = cv2.erode(img,(5,5),iterations = 3)
#img = cv2.dilate(img,None,iterations = 1)


while(1):
	r = cv2.getTrackbarPos('Threshold','trackbar')
	k = cv2.waitKey(1) & 0xFF
	e = cv2.getTrackbarPos('Erosion','trackbar')
	d = cv2.getTrackbarPos('Dilation','trackbar')
	kernVal= cv2.getTrackbarPos('Kernel','trackbar')
	kernel = np.ones((kernVal,kernVal),np.uint8)
	
    
	ret,th3 = cv2.threshold(img,r,255,cv2.THRESH_BINARY)
	#blur stuff
	b=cv2.getTrackbarPos('Blur','trackbar')
	#th3=cv2.medianBlur(th3,b)
	#threshold shizz
	th3 = cv2.erode(th3,kernel,iterations = e)
	th3 = cv2.dilate(th3,kernel,iterations = d)
	#filtered=imutils.resize(th3,width=648)
	cv2.GaussianBlur(th3,(21,21),0)
	filtered=imutils.resize(th3,width=432,height=324)
	cv2.imshow('Doublefiltered',filtered)


	if k==27:
		break
	elif k== ord('s'):
		cv2.destroyWindow('trackbar')
    	#name = raw_input("Enter file name:") 
    	cv2.imwrite('threshed.jpg',th3)
	
cv2.destroyAllWindows() 


#arunav konwar
#arunavkonwar@gmail.com

