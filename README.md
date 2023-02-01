# Computer-Design-Competition
This repository is used for our team to synchronous progress

该项目最终目标是完成一个集多功能于一体的计算机助理





## 使用方法

下载好该包后，进入目录中，选择好运行环境并运行以下命令即可

```
pip install -r requriements.txt
```





## 隔空控制鼠标

这里我们采取Google Research开发的MediaPipe完成对手部特征点的定位

我们选择完成鼠标的四个功能，现对功能的使用做如下说明

* 移动鼠标：握拳并滑动可实现页面滚动
* 滚标滚轮：张开五指，并上下欢动，即可移动鼠标
* 左键：握拳并伸出大拇指可左键鼠标当前位置
* 右键：握拳并深处食指可右键鼠标当前位置

整体部分采取多线程并行加速
