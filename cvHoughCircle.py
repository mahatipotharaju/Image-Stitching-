import cv2
import cv2.cv as cv
import numpy as np
import imutils

img = cv2.imread('owl1.jpg')
img=imutils.resize(img,width=432,height=324)
#img = cv2.medianBlur(img,5)
cimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

circles = cv2.HoughCircles(cimg, cv2.cv.CV_HOUGH_GRADIENT, 1.2, 200)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    center=(i[0],i[1])
    radius=i[2]
  #  cv2.circle(img,(i[0],i[1]),i[2],(0,0,0),2)
    # draw the center of the circle
  #  cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)
    print i[0],i[1]

center=(center[0],center[1])
radius=radius
print center
print radius

mask=np.zeros(img.shape[:], dtype=np.uint8)
cv2.circle(mask,center,radius,(255,255,255),thickness=-1)

# the mask will be a bgr image
# has to be converted to grayscale for threshholding
mask=cv2.cvtColor(mask,cv2.COLOR_BGR2GRAY)


# threshholding the grayscale image to get a binary image, with max_value 1
ret,mask=cv2.threshold(mask,10,1,cv2.THRESH_BINARY)

# the mask is multiplied with all 3 channels of the original image 
b=np.multiply(img[:,:,0],mask)
g=np.multiply(img[:,:,1],mask)
r=np.multiply(img[:,:,2],mask)

# img_final combines these 3 seperated channels to get the final Fundus image
img_final=np.zeros(img.shape[:])
img_final=np.uint8(img_final)
img_final[:,:,0]=b
img_final[:,:,1]=g
img_final[:,:,2]=r

# the mask and final image are resized for displaying on screen
#mask=imutils.resize(mask,width=648)
filtered=imutils.resize(img_final,width=648)

cv2.imshow('detected circles',img)
cv2.imshow('mask',mask)
cv2.imshow('filtered',filtered)
cv2.imwrite('owlFiltered.jpg',filtered)


#cv2.imshow('detected circles',img)
cv2.waitKey(0)
cv2.destroyAllWindows() 