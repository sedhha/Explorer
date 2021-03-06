import cv2
import numpy as np
#cam=cv2.VideoCapture(0)
img=cv2.imread('11.jpg')
newX,newY = img.shape[1]*0.6, img.shape[0]*0.6
img = cv2.resize(img,(int(newX),int(newY)))
cnt=0
def nothing(x):
    pass
cv2.namedWindow('Properties')
cv2.resizeWindow('Properties',400,400)
cv2.createTrackbar('H-min','Properties',0,255,nothing)
cv2.createTrackbar('H-max','Properties',0,255,nothing)
cv2.createTrackbar('S-min','Properties',0,255,nothing)
cv2.createTrackbar('S-max','Properties',0,255,nothing)
cv2.createTrackbar('V-min','Properties',0,255,nothing)
cv2.createTrackbar('V-max','Properties',0,255,nothing)
cv2.createTrackbar('Noise','Properties',0,200,nothing)

def color_filter(img,lower,upper,noise):
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    filt=cv2.inRange(hsv,lower,upper)
    kernel=np.ones((noise,noise),dtype=np.float32)/(noise*noise)
    filt=cv2.morphologyEx(filt,cv2.MORPH_OPEN,kernel)
    cv2.imshow('Contour ',filt)
    colorfilt=cv2.bitwise_and(img,img,mask=filt)
    cv2.imshow('filter color',filt)
    return(colorfilt,filt)
def draw_contour(image,filt):
    im2, contours, hierarchy = cv2.findContours(filt,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    temp=image
    cv2.drawContours(temp, contours, -1, (0,255,0), 1)
    cv2.imshow('contours drawn',temp)
    return(temp,contours)

def Label(image,contours):
    print(len(contours))
    if len(contours)>10:
        pass
    for i in range(len(contours)):
        cnt=contours[i]
        M=cv2.moments(cnt)
        if M['m00']!=0:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            area = cv2.contourArea(cnt)
            print(area,cx,cy)
            #image=texting(image,cx,cy,area)
            cv2.putText(image,str(area),(cx,cy), cv2.FONT_HERSHEY_SIMPLEX, 0.4,(255,255,255),1)
            try:
              cv2.imshow('image_texted',image)
              return(image)
            except:
                pass
        
    
while 1:
    H_min=cv2.getTrackbarPos('H-min','Properties')
    H_max=cv2.getTrackbarPos('H-max','Properties')
    S_min=cv2.getTrackbarPos('S-min','Properties')
    S_max=cv2.getTrackbarPos('S-max','Properties')
    V_min=cv2.getTrackbarPos('V-min','Properties')
    V_max=cv2.getTrackbarPos('V-max','Properties')
    noise=cv2.getTrackbarPos('Noise','Properties')
    lower=np.array((H_min,S_min,V_min))
    upper=np.array((H_max,S_max,V_max))
    image,filt=color_filter(img,lower,upper,noise)
    image_contour,contours=draw_contour(image,filt)
    image_Lb=Label(image_contour,contours)
    k=cv2.waitKey(1)
    if k & 0xFF == ord('q'):
        break
    if k==ord('w'):
        cnt=cnt+1
        cv2.imwrite('Image-0'+str(cnt)+'.jpg',image)
        cv2.imwrite('Image_filt0'+str(cnt)+'.jpg',filt)
        cv2.imwrite('Image_contour0'+str(cnt)+'.jpg',image_contour)
        cv2.imwrite('Image_Lb0'+str(cnt)+'.jpg',image_Lb)

cv2.destroyAllWindows()
