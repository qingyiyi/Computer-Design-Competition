# Computer-Design-Competition
This repository is used for our team to synchronous progress

该项目最终目标是完成一个集多功能于一体的计算机助理





## 使用方法

下载好该包后，需要安装ffmpeg命令

> Windows系统如下安装
>
> 以管理员身份打开powershell，并运行以下命令
>
> ```
> Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
> ```
>
> 接着在cmd中输入以下命令
>
> ```
> choco install ffmpeg
> ```



> Linux系统如下安装
>
> ```shell
> sudo apt update && sudo apt install ffmpeg
> ```



进入项目目录中，选择好运行环境并运行以下命令即可

```
pip install -r requriements.txt
```

> 注意关闭vpn
>
> 笔者使用python版本是3.9



### 手势控制鼠标

该部分主要依赖Mediapip框架，通过得到的手部21个关键点的三维坐标，再以坐标计算每个手指角度判断手指的弯曲情况，从而得到手势判断，之后结合pyautoGui即可实现对电脑的控制。

* 移动鼠标：握拳并滑动可实现页面滚动
* 滚标滚轮：张开五指，并上下欢动，即可移动鼠标
* 左键：握拳并伸出大拇指可左键鼠标当前位置
* 右键：握拳并深处食指可右键鼠标当前位置



### 画面描述

为了帮助不能看见的人使用电脑，我们加入了画面描述系统，您只需要说出带有```描述```关键词的语句，计科触发该功能，帮助您将屏幕上的照片，绘画，或者电影等转化为描述性语言，此后无需专门开发盲人电影，借助该软件您就可以直接将任何电影变成盲人电影。



### 聊天系统

我们的软件接入了最新的chatgpt系统，它可以模拟人的行为，为您提供最完善的聊天体系。
