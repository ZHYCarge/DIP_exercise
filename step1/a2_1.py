import cv2
import matplotlib.pyplot as plt
import numpy as np

"""
2.1 要求:
用摄像头抓取实验者自己的彩色图像，转换为灰度图像，
然后在屏幕的8个区域中分别显示该图像的256、128、64、32、16、8、4、2色图像，
并存成磁盘文件，对比说明灰度分辨率对图像的影响；
"""


images = []
tags = ['256', '128', '64', '32', '16', '8', '4', '2']
cap = cv2.VideoCapture(1)
while True:
    status, image = cap.read()
    if status is True:
        cv2.imshow("image", image)
        high, width = image.shape[:2]
        key = cv2.waitKey(1)
        if key & 0xFF == ord("q"):
            break

        elif key & 0xFF == ord("s"):
            images.append(cv2.cvtColor(image, cv2.COLOR_RGB2GRAY))
            for a in range(7):
                images.append(np.zeros([480, 640, 3], np.uint8))
            print(len(images))
            for i in range(high):
                for j in range(width):
                    p = images[0][i, j]  # 256色图像（灰度）
                    if (p + 2) % 2 == 1:
                        images[7][i, j] = int(p / 2 + 1) * 2 - 1    # 制作2色图像
                    if (p + 4) % 4 != 0:
                        images[6][i, j] = int(p / 4 + 1) * 4 - 1    # 制作4色图像
                    if (p + 8) % 8 != 0:
                        images[5][i, j] = int(p / 8 + 1) * 8 - 1    # 制作8色图像
                    if (p + 16) % 16 != 0:
                        images[4][i, j] = int(p / 16 + 1) * 16 - 1  # 制作16色图像
                    if (p + 32) % 32 != 0:
                        images[3][i, j] = int(p / 32 + 1) * 32 - 1  # 制作32色图像
                    if (p + 64) % 64 != 0:
                        images[2][i, j] = int(p / 64 + 1) * 64 - 1  # 制作64色图像
                    if (p + 128) % 128 != 0:
                        images[1][i, j] = int(p / 128 + 1) * 128 - 1    # 制作128色图像
            fig = plt.figure(num=1)
            for a in range(8):
                print(a)
                plt.subplot(2, 4, a+1)
                plt.title(f'the {tags[a]} image')
                plt.imshow(images[a], cmap="gray")
            plt.show()
            fig.savefig("./output/a2_1.jpg")
            break
    else:
        break

cap.release()
