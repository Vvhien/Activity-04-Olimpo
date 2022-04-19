import cv2
filepath ="donna.jpg"
image = cv2.imread(filepath,1)
cv2.imshow("donna",image)
cv2.waitKey(0)
cv2.destroyAllWindows()