
## Opencv读写文件的路径对utf-8（包括中文路径）的支持

**Support opencv reading and writing image using utf-8 paths.**

### Install

Install using pip:

```commandline
pip install opencv-utf-8
```

or:

```commandline
pip install -i https://pypi.org/simple/ opencv-utf-8
```

### Usage

```python
import cv2_ext
import cv2

img = cv2_ext.imread(r'E:\壁纸\pc-twoup-weibu.jpg')
cv2.imshow('', img)
cv2.waitKey()

cv2_ext.imwrite(r'E:\壁纸\pc-twoup-weibu_中文.tif', img)
```


Thanks.

Good luck bro.