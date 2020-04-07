import cv2

#Reading image 2nd argument 0-grayscale 1-rgb -1-as it is
img = cv2.imread('lena.jpg',1)

#Displays the image
cv2.imshow('image',img)
a = cv2.waitKey(0)          #this helps the image window to be available at custom time 0-Close Manually 
#cv2.destroyAllWindows()    #closes the window

#If user presses s key the image will be copied and esc then window will be closed
if a==27:
    cv2.destroyAllWindows()
elif a==ord('s'):
    cv2.imwrite('lena_copy.jpg',img)  #save the image with specified filename
    cv2.destroyAllWindows()