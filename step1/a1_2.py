import cv2
import matplotlib.pyplot as plt


"""
要求：比较阈值结果并显示
例如：
InImg=imread(‘d:\DirName\demoImg_InPut.bmp’)
bw = im2bw (InImg,0.5)		比较不同阈值的结果
subplot(1，2，1)；imshow(InImg);显示彩色图像于屏幕第一块区域
subplot(1，2，2)；imshow(bw) ;显示二值图像于屏幕第二块区域
"""

image = plt.imread("./others/s1.jpeg")  # 读入图像
bw = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) # 调节为灰度图像
bw = cv2.threshold(bw, 127, 255, cv2.THRESH_BINARY)[1]  # 调节为二值化图像

plt.subplot(1, 2, 1)
plt.title("Origin image")
plt.imshow(image)
plt.subplot(1, 2, 2)
plt.title("binary image")
plt.imshow(bw, cmap='gray')
plt.show()