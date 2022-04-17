import cv2
import matplotlib.pyplot as plt

import skimage
from skimage import util, filters
from skimage.morphology import disk

'''
4.3要求:
将自己的彩色照片转换为灰度图像，
对其分别加入椒盐噪声、高斯噪声、斑点噪声，
然后用中值滤波、均值模板、拉普拉斯模板分别对其
滤波，观察、对比其结果。
'''


# 摄像头捕获
def camera():
    cap = cv2.VideoCapture(1)
    while True:
        type, img = cap.read()
        if not type:
            break
        cv2.imshow("img_RGB", img)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('s'):
            img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
            cap.release()
            cv2.destroyAllWindows()
            return img


# 椒盐噪声产生
def addsalt_pepper(img, SNR=0.8):
    return skimage.util.random_noise(img, mode="s&p")
    # img_ = img.copy()
    # h, w = img_.shape
    # mask = np.random.choice((0, 1, 2), size=(h, w), p=[SNR, (1 - SNR) / 2., (1 - SNR) / 2.])
    # img_[mask == 1] = 255    # 盐噪声
    # img_[mask == 2] = 0      # 椒噪声
    # return img_


# 高斯噪声产生
# https://blog.csdn.net/qq_45769063/article/details/107137025
def gasuss_noise(img, mean=0, var=0.001):
    return skimage.util.random_noise(img, mode="gaussian")
    # image = np.array(image/255, dtype=float)#将原始图像的像素值进行归一化，除以255使得像素值在0-1之间
    # noise = np.random.normal(mean, var ** 0.5, image.shape)#创建一个均值为mean，方差为var呈高斯分布的图像矩阵
    # out = image + noise#将噪声和原始图像进行相加得到加噪后的图像
    # if out.min() < 0:
    #     low_clip = -1.
    # else:
    #     low_clip = 0.
    # out = np.clip(out, low_clip, 1.0)#clip函数将元素的大小限制在了low_clip和1之间了，小于的用low_clip代替，大于1的用1代替
    # out = np.uint8(out*255)#解除归一化，乘以255将加噪后的图像的像素值恢复
    # #cv.imshow("gasuss", out)
    # # noise = noise*255 # 噪声模板
    # return out


# 斑点噪声
def speckle_noise(img):
    return skimage.util.random_noise(img, mode="speckle")


# 优化
def optimize(img_o, img):
    # 原始图像
    plt.subplot(2, 3, 1)
    plt.title("origin image")
    plt.imshow(img_o, cmap="gray")

    # image_m = cv2.medianBlur(img, 3) # 3代表3*3矩阵模板（大概）
    image_m = filters.median(img, disk(5))
    plt.subplot(2, 3, 4)
    plt.title("median filter")
    plt.imshow(image_m, cmap="gray")

    image_b = cv2.blur(img, (5, 5))  # 5*5矩阵模板
    plt.subplot(2, 3, 5)
    plt.title("average filter")
    plt.imshow(image_b, cmap="gray")

    image_l = cv2.Laplacian(img, cv2.CV_64F, ksize=15)
    # https://docs.opencv.org/3.0-last-rst/modules/imgproc/doc/filtering.html#laplacian
    # https://blog.csdn.net/luoluo3664/article/details/103354195
    plt.subplot(2, 3, 6)
    plt.title("laplace transformation")
    plt.imshow(image_l, cmap="gray")
    plt.show()


if __name__ == '__main__':
    image = camera()

    # 椒盐噪声图像
    plt.figure(1)
    image_s = addsalt_pepper(image, 0.8)  # https://blog.csdn.net/u011995719/article/details/83375196
    plt.subplot(2, 3, 3)
    plt.title("salt_pepper")
    plt.imshow(image_s, cmap="gray")
    optimize(image, image_s)

    # 高斯噪声
    plt.figure(2)
    image_g = gasuss_noise(image)
    plt.subplot(2, 3, 3)
    plt.title("gaussian noise")
    plt.imshow(image_g, cmap="gray")
    optimize(image, image_g)

    # 斑点噪声
    plt.figure(3)
    image_sp = speckle_noise(image)
    plt.subplot(2, 3, 3)
    plt.title("speckle noise")
    plt.imshow(image_sp, cmap="gray")
    optimize(image, image_sp)
