import os
import cv2

'''
找国旗

- 罗马尼亚： 3-2 左至右为蓝、黄、红 蓝色浅
- 乍得： 3-2  左至右为蓝、黄、红 蓝色深

- 荷兰： 3-2 上而下的红、白、蓝
- 卢森堡： 3-2 上而下的红、白、蓝 蓝横条为天蓝色，比荷兰浅

-印度尼西亚： 3-2 上红下白二色横条旗
-意大利： 3-2 左-右 绿、白、红

-摩纳哥 5-4 上红下白二色横条旗

-波兰： 8-5 二色横条为上白下红

-爱尔兰： 2-1

-瑞士：1-1 红底白十字
-梵蒂冈：1-1 左黄色，右边白色配图片
'''


flags = os.listdir('./flag/')
need_flag = []
for flag in flags:
    image = cv2.imread(f'./flag/{flag}')
    h= image.shape[0]   #宽
    w= image.shape[1]   #长
    if h == w:
        x, y, z = image[int(h / 4) * 3][int(w / 4) * 3]
        if z == 255 and y == 255 and z == 255:
            need_flag.append(f"梵蒂冈的国旗图片是:\"{flag}\"")
        else:
            need_flag.append(f"瑞士的国旗图片是:\"{flag}\"")
    elif 2*h == w:
        need_flag.append(f"爱尔兰的国旗图片是:\"{flag}\"")
    elif 5*w == 8*h:
        need_flag.append(f"波兰的国旗图片是:\"{flag}\"")
    elif 4*w == 5*h:
        need_flag.append(f"摩纳哥的国旗图片是:\"{flag}\"")
    elif abs(float(h/w)) < 2: # BGR
        x, y, z = image[int(h/6)*5][int(w/2)]
        # print(image[int(h / 6) * 5][int(w / 2)])
        if x==255 and y ==255 and z == 255:
            x,y,z = image[int(h/4)][int(w/2)]
            # print(image[int(h / 4)][int(w / 2)])
            if x == 255 and y == 255 and z == 255:
                need_flag.append(f"意大利的国旗图片是:\"{flag}\"")
            else:
                need_flag.append(f"印度尼西亚的国旗图片是:\"{flag}\"")
        elif z == 0:
            need_flag.append(f"卢森堡的国旗图片是:\"{flag}\"")
        elif 30 > x > 0:
            need_flag.append(f"罗马尼亚的国旗图片是:\"{flag}\"")
        elif x == 0:
            need_flag.append(f"乍得的国旗图片是:\"{flag}\"")
        else:
            need_flag.append(f"荷兰的国旗图片是:\"{flag}\"")

for a in need_flag:
    print(a)