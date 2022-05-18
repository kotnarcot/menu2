import cv2


img = cv2.imread("1.jpg")


profile = cv2.CascadeClassifier("profile.xml")
result = profile.detectMultiScale(img, scaleFactor=3, minNeighbors=20) #вместо (a-scaleFactor малое число), вместо (a-minNeighbors любое число)


print(result)

for (x,y,w,h) in result:
    cv2.rectangle(img, (x,y),(x+w, y+h), (0,0,255),thickness= 2)

cv2.imshow("Result",img)
cv2.waitKey(0)