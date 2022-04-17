import cv2
import matplotlib.pyplot as plt
import numpy as np

"""
4.1 要求:
将通过摄像头采集的自己的彩色照片转换为灰度图像，
a)绘制灰度图像的灰度直方图；
b)对灰度图进行反转变换，再绘制其直方图，观察前后直方图的关系；
c)对灰度图进行直方图均衡化，对比前后直方图。
"""

# 参考：https://blog.csdn.net/qq_40728667/article/details/110334988

cap = cv2.VideoCapture(1)
while True:
    type, image = cap.read()
    if not type:
        break
    cv2.imshow("image_RGB", image)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("h"):
        image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        cap.release()
        cv2.destroyAllWindows()
        break
img_ravel = image.ravel()

# 显示灰度直方图
plt.subplot(1, 3, 1)
plt.title("grey level histogram")
plt.hist(img_ravel, 256, [0, 256])

# 灰度图片反转
image_r = np.zeros([480, 640], np.uint8)
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        image_r[i][j] = 255 - image[i][j]
image_r_r = image_r.ravel()
plt.subplot(1, 3, 2)
plt.title("Invert the histogram")
plt.hist(image_r_r, 256, [0, 256])

# 直方图均衡化

image_e = cv2.equalizeHist(image)
image_e_r = image_e.ravel()
plt.subplot(1, 3, 3)
plt.title("histogram equalization")
plt.hist(image_e_r, 256, [0, 256])
plt.show()
