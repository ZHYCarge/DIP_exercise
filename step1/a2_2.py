import cv2
import matplotlib.pyplot as plt

"""
2.2 要求:
用摄像头抓取实验者自己的彩色图像，转换为灰度图像，
然后在屏幕的6个区域中分别显示该图像缩小为原图的1、1/2、1/4、1/8、1/16、1/32大小的图，
并存成磁盘文件，对比说明空间分辨率对图像的影响；
"""

cap = cv2.VideoCapture(1)
images = []
tags = [1, 1/2, 1/4, 1/6, 1/8, 1/16, 1/32]
while True:
    status, image = cap.read()
    if status is True:
        cv2.imshow("image", image)
        high, width = image.shape[:2]
        key = cv2.waitKey(1)
        if key & 0xFF == ord("q"):
            break
        elif key & 0xFF == ord('s'):
            image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
            for a in range(6):
                images.append(cv2.resize(image, (int(width*tags[a]), int(high*tags[a]))))
            fig = plt.figure(num=1)
            for a in range(6):
                plt.subplot(2, 3, a+1)
                plt.title(f"{round(tags[a],2)} image")
                plt.imshow(images[a], cmap="gray")
            plt.show()
            fig.savefig("./output/a2_2.jpg")
            break
    else:
        break

