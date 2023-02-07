# Computer-Design-Competition
This repository is used for our team to synchronous progress

该项目最终目标是完成一个集多功能于一体的计算机助理





## 使用方法

下载好该包后，进入目录中，选择好运行环境并运行以下命令即可

```
pip install -r requriements.txt
```





### 手势控制鼠标

该部分主要依赖Mediapip框架，通过得到的手部21个关键点的三维坐标，再以坐标计算每个手指角度判断手指的弯曲情况，从而得到手势判断，之后结合pyautoGui即可实现对电脑的控制。

* 移动鼠标：握拳并滑动可实现页面滚动
* 滚标滚轮：张开五指，并上下欢动，即可移动鼠标
* 左键：握拳并伸出大拇指可左键鼠标当前位置
* 右键：握拳并深处食指可右键鼠标当前位置
