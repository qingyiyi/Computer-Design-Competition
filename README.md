# Computer-Design-Competition
This repository is used for our team to synchronous progress

该项目最终目标是完成一个集多功能于一体的计算机助理



## 隔空控制鼠标

这里我们采取Google Research开发的MediaPipe完成对手部特征点的定位

我们选择完成鼠标的四个功能，现对功能的使用做如下说明

* 移动鼠标：张开五指，即可移动鼠标
* 滚标滚轮：握拳并上下滑动可实现页面滚动
* 左键：弯曲食指可左键鼠标当前位置
* 右键：弯曲中指可右键鼠标当前位置

整体部分采取多线程并行加速
