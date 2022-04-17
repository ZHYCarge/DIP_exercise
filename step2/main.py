import re

from flask import Flask,render_template,request,redirect,url_for
from werkzeug.utils import secure_filename
import os
# import imagehash
import cv2

app = Flask(__name__)

#均值哈希算法
def aHash(img):
    #缩放为8*8
    img=cv2.resize(img,(8,8),interpolation=cv2.INTER_CUBIC)
    #转换为灰度图
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #s为像素和初值为0，hash_str为hash值初值为''
    s=0
    hash_str=''
    #遍历累加求像素和
    for i in range(8):
        for j in range(8):
            s=s+gray[i,j]
    #求平均灰度
    avg=s/64
    #灰度大于平均值为1相反为0生成图片的hash值
    for i in range(8):
        for j in range(8):
            if  gray[i,j]>avg:
                hash_str=hash_str+'1'
            else:
                hash_str=hash_str+'0'
    return hash_str


#Hash值对比
def cmpHash(hash1,hash2):
    n=0
    #hash长度不同则返回-1代表传参出错
    if len(hash1)!=len(hash2):
        return -1
    #遍历判断
    for i in range(len(hash1)):
        #不相等则n计数+1，n最终为相似度
        if hash1[i]!=hash2[i]:
            n=n+1
    return 100-n


@app.route('/', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        basepath = os.path.dirname(__file__)  # 当前文件所在路径
        # print(basepath)
        # print(f.filename)
        upload_path = os.path.join(basepath, 'static',f.filename)
        # 注意：没有的文件夹一定要先创建，不然会提示没有该路径
        # print(upload_path)
        upload_path = os.path.abspath(upload_path) # 将路径转换为绝对路径
        # print(upload_path)
        file = upload_path
        if os.path.exists('./static/1.png'):
            os.remove('./static/1.png')
        f.save(upload_path)
        os.rename(f'./static/{f.filename}','./static/1.png')
        # return redirect(url_for('upload'))


        result_a = []
        hash1 = aHash(cv2.imread('./static/1.png'))
        flags = os.listdir('./static/flag/')
        for flag in flags:
            hash2 = aHash(cv2.imread(f'./static/flag/{flag}'))
            result_a.append(flag + "-"+ str(cmpHash(hash1,hash2)))
        result_a = sorted(result_a,reverse = True, key=lambda info: (int(re.findall(r'-(\d+)', info)[0])))
        result = result_a[0].split("-")
        return render_template('solve.html',resulta =result_a ,where=result[0],passes=result[1])
    return render_template('upload.html')


if __name__ == '__main__':
    app.run(debug=True)