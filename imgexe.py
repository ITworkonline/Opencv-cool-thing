import cv2

img = cv2.imread('/Users/skidnp/Desktop/1130/file.jpg')
#HSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv= cv2.namedWindow("Image")
cv2.imshow("Image", img)
cv2.waitKey (0)
cv2.destroyAllWindows()
