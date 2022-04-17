import cv2

import step1.a2_3 as B

image1 = B.BWBand(21, 31)
image2 = B.BWBand(21, 61)
cv2.imshow("image", image1)
cv2.imshow("image1", image2)
cv2.waitKey(0)
