#!/GPFS/zhangli_lab_permanent/zhuqingjie/env/py3_tf2/bin/python
'''
@Time    : 20/11/05 下午 01:56
@Author  : zhuqingjie 
@User    : zhu
@FileName: setup.py
@Software: PyCharm
'''
import setuptools
import cv2_ext

'''
pip install -i https://pypi.org/simple/ opencv-utf-8 
'''

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="opencv-utf-8",
    version=cv2_ext.__version__,
    author="azzhu",
    author_email="zhu.qingjie@qq.com",
    description="Support opencv read and write image using utf-8 paths",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/azzhu/opencv-utf-8",
    license='MIT',
    install_requires=[
        'numpy'
    ],
    packages=setuptools.find_packages(),
    project_urls={
        "Source Code": "https://github.com/azzhu/opencv-utf-8",
        "Bug Tracker": "https://github.com/azzhu/opencv-utf-8/issues",
        "Documentation": "https://github.com/azzhu/opencv-utf-8",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
)
