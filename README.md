# OpenCV 学习笔记
---
##### 所有学习内容均来自网络，感谢各位大神的无私分享！

##### 主要原贴地址:[Daetalus](http://blog.csdn.net/sunny2038/article/category/904451)和[MoreWindows]()

##### 以下是介绍学习的章节，和每部分的学习内容
---
### 安装相关 => [点击这里](http://blog.csdn.net/insthink/article/details/51338839)

- ### test1 => 图像的载入、显示和保存

- ### test2 = > 图像元素的访问、通道分离与合并

- ### test3 => 忘记是啥了.....好像没啥用

- ### test4 => 形态处理，边缘检测
    - ##### 定义结构元素([test4.py](test4/test4.py))
        ###### 形态学处理的核心就是定义结构元素
        ###### 在OpenCV-Python中，可以使用其自带的getStructuringElement函数，也可以直接使用NumPy的ndarray来定义一个结构元素。
        ###### 首先来看用getStructuringElement函数定义一个结构元素：
        ``` python
        element = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))
        ```
        ###### 也可以用NumPy来定义结构元素，如下：
        ``` python
        NpKernel = np.uint8(np.zeros((5,5)))  
        for i in range(5):  
            NpKernel[2, i] = 1 #感谢chenpingjun1990的提醒，现在是正确的  
            NpKernel[i, 2] = 1  
        ```
        腐蚀和膨胀
        ``` python 
        eroded = cv2.erode(img,kernel) 
        dilated = cv2.dilate(img,kernel)  
        ```
    - ##### 开运算和闭运算([test4-1.py](test4/test4-1.py))
        ###### 了解形态学基本处理的同学都知道，开运算和闭运算就是将腐蚀和膨胀按照一定的次序进行处理。
        ###### 但这两者并不是可逆的，即先开后闭并不能得到原先的图像。
        ``` python 
        #闭运算  
        closed = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)   
        #开运算  
        opened = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)  
        ```
    - ##### 形态学运算检测边和角点([test4-2.py](test4/test4-2.py))
    - ##### 检测拐角([test4-3.py](test4/test4-3.py))
        ###### 与边缘检测不同，拐角的检测的过程稍稍有些复杂。
        ###### 但原理相同，所不同的是先用十字形的结构元素膨胀像素，这种情况下只会在边缘处“扩张”，角点不发生变化。
        ###### 接着用菱形的结构元素腐蚀原图像，导致只有在拐角处才会“收缩”，而直线边缘都未发生变化。
        ###### 第二步是用X形膨胀原图像，角点膨胀的比边要多。
        ###### 这样第二次用方块腐蚀时，角点恢复原状，而边要腐蚀的更多。
        ###### 所以当两幅图像相减时，只保留了拐角处。。
    - ##### 图像变换之Canny算子边缘检测([test4-4.py](test4/test4-4.py))
        ###### Canny是常用的边缘检测方法，其特点是试图将独立边的候选像素拼装成轮廓[详细介绍](test4/Canny.md)。
