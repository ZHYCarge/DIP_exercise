import os

import cv2

"""
2.4要求 :
某公司收到一份订单，要求印刷若干国旗图片（参见群文件的“国旗.zip”）。
但是甲方发邮件的人习惯太糟糕了，附件图片文件名根本是无法识别的数字、字母。
请编程找出其中的瑞士和梵蒂冈国旗图像。已知：
1）全世界只有瑞士和梵蒂冈的国旗是正方形的；
2）瑞士国旗是红底上的白色十字；梵蒂冈国旗左半边是黄色，右边是白色背景上的图案。
"""

flags = os.listdir('./flag/')
need_flag = []
for flag in flags:
    image = cv2.imread(f'./flag/{flag}')
    if image.shape[0] == image.shape[1]:
        x, y, z = image[int(image.shape[0] / 4) * 3][int(image.shape[1] / 4) * 3]
        if z == 255 and y == 255 and z == 255:
            need_flag.append(f"梵蒂冈的国旗图片是:\"{flag}\"")
        else:
            need_flag.append(f"瑞士的国旗图片是:\"{flag}\"")
    else:
        continue
print(need_flag)
