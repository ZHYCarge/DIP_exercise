import cv2
import numpy as np


"""
2.3.2 要求:
编写一个函数BWBand(w，h)（请勿编写脚本程序，必须是函数）。
该函数用于产生一个数组，该数组代表长201、高321的8比特灰度图像，图像背景是纯黑色，
中间有一个纯白色的矩形（长w、高h），w、h是函数的参数。将BWBand(7,11)对应的图像显示在屏幕上并存盘。
（请注意保存该函数文件，以后的实验会继续使用）

"""


def BWBand(w, h):
    image = np.zeros([321, 201], np.uint8)
    print(image.shape)
    x = int(image.shape[0] / 2) + 1 - int(w / 2)
    y = int(image.shape[1] / 2) + 1 - int(h / 2)
    for i in range(w):
        for j in range(h):
            image[x + j, y + i] = 255

    return image


if __name__ == '__main__':
    image = BWBand(7, 11)
    cv2.imshow("image", image)
    cv2.imwrite("./output/2_3.png", image, [cv2.IMWRITE_PNG_STRATEGY, 10])
    cv2.waitKey(0)
