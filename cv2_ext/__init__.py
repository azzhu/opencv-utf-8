#!/GPFS/zhangli_lab_permanent/zhuqingjie/env/py3_tf2/bin/python
'''
@Time    : 20/11/16 下午 01:28
@Author  : zhuqingjie 
@User    : zhu
@FileName: __init__.py.py
@Software: PyCharm
'''
import cv2
import numpy as np

__version__ = '0.0.4'

__doc__ = '借助numpy实现opencv读写图像对中文路径的支持。'


def imread(p):
    data = np.fromfile(p, dtype=np.uint8)
    return cv2.imdecode(data, cv2.IMREAD_UNCHANGED)


def imwrite(p, img):
    ext = '.' + p.split('.')[-1]
    temp = cv2.imencode(ext=ext, img=img)
    temp[1].tofile(p)
