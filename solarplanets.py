import os 
import shutil  
import cv2

img = cv2.imread("solar-system.jpg")

textToShow = "earth"
cv2.putText(img, textToShow, (300, 200), fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale = 1, color = (0, 0, 255))

textToShow = "Mars"
cv2.putText(img, textToShow, (400, 200), fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale = 1, color = (0, 0, 255))

textToShow = "Venus"
cv2.putText(img, textToShow, (200, 200), fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale = 1, color = (0, 0, 255))

textToShow = "Mercury"
cv2.putText(img, textToShow, (75, 200), fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale = 1, color = (0, 0, 255))

textToShow = "Jupiter"
cv2.putText(img, textToShow, (500, 200), fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale = 1, color = (0, 0, 255))

textToShow = "Saturn"
cv2.putText(img, textToShow, (700, 200), fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale = 1, color = (0, 0, 255))

textToShow = "Uranus"
cv2.putText(img, textToShow, (900, 200), fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale = 1, color = (0, 0, 255))

textToShow = "Neptune"
cv2.putText(img, textToShow, (1100, 200), fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale = 1, color = (0, 0, 255))

cv2.imshow("Solar System", img)

cv2.waitKey(0)
