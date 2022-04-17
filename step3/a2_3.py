import cv2
import matplotlib.pyplot as plt
import numpy as np

'''
要求：
将自己的彩色照片转换为灰度图像，对其加入椒盐噪声，然后设计数字图像频域低通滤波器对其滤波，对比其结果，
Refence：
https://blog.csdn.net/baidu_41902768/article/details/95058390
'''

img = cv2.imread("./1.jpeg")

# img = np.array(img)

height, width, c = img.shape

fft = np.fft.fft2(img)
fftshift = np.fft.fftshift(fft)

cutstop = 300

for i in range(height):
    for j in range(width):
        if (i - (height - 1) / 2) ** 2 + (j - (width - 1) / 2) ** 2 >= cutstop ** 2:
            fftshift[i, j] = 0

fftshift = np.fft.ifftshift(fftshift)
ifft = np.fft.ifft2(fftshift)
# new = np.zeros([height, width], np.uint8)

# for i in range(height):
#     for j in range(width):
#         print(new[i,j])
#         print(ifft[i,j].real)
#         new = ifft.real

image = ifft.real
plt.imshow(image)
plt.show()
# new_im = Image.fromarray(new)
# new_im.save("C:/Users/60214/Desktop/python_work/DigitalExecution/girl1.jpg")
