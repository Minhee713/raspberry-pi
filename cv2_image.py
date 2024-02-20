import cv2

img = cv2.imread('photo.png')

cv2.imshow('photo', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
