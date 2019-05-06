
import cv2
import argparse
import numpy as np
cap = cv2.VideoCapture(1)

while True:
    _, frame = cap.read()

    laplacian = cv2.Laplacian(frame, cv2.IMREAD_GRAYSCALE, 255)

    cv2.imshow('original',frame)
    cv2.imshow('laplacian',laplacian)
    #edged_frame = cv2.Canny(frame,100,200)
    #cv2.imshow('Edges',edged_frame)
    
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
      break

cv2.destroyAllWindows()
cap.release()
