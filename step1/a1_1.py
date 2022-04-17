import cv2
import matplotlib.pyplot as plt

"""
要求：显示彩色图像于屏幕第一块区域；显示灰度图像于屏幕第二块区域；输出灰度图像
InImg=imread(‘d:\DirName\demoImg_InPut.bmp’);
I=rgb2gray(InImg);
subplot(1，2，1)；imshow(InImg);显示彩色图像于屏幕第一块区域
subplot(1，2，2)；imshow(I);显示灰度图像于屏幕第二块区域
ImWrite (I,‘d:\DirName\demoImg_outPut.bmp’)
"""

image = plt.imread("./others/s1.jpeg")  # 读入图像

image_g = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)   # 将图像转换为灰度图像

plt.subplot(1, 2, 1)    # 建立一个1*2的框，使用第一块

plt.title("Origin image")
plt.imshow(image)  # 显示原始图像

plt.subplot(1, 2, 2)    # 建立一个1*2的框，使用第二块
plt.title("gray image")
plt.imshow(image_g, cmap='gray')    # 显示灰度图像

plt.show()  # 展示

cv2.imwrite("./output/s1.png", image_g, [cv2.IMWRITE_PNG_STRATEGY, 10]) # 输出灰度图像
