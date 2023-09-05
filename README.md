# 写在最前面

本项目是北京理工大学人工智能&未来精工技术的大三小学期成果。整个代码，除了涉及opencv的部分均可在windows，linux上几乎完美地运行。视频通话部分只在windows上成功测试过。

# 配置

1. 设备需要有摄像头与摄像头驱动，如果你不用人脸识别&视频通话，那无所谓。

2. 有关Pyside和whisper，请参考官方在github上的安装流程

   https://github.com/zhiyiYo/PyQt-Fluent-Widgets/tree/PySide2

   https://github.com/openai/whisper

3. 由于PyAudio库较为古老，直接pip install可能报错

   请尝试

   ```bash
   sudo apt-get install portaudio19-dev
   
   sudo apt-get install python3-all-dev
   
   pip install pyaudio
   ```

   

4. 受限于设备，我们没有测试linux端的视频通话。以下是linux系统可以尝试一下的，不保证成功

   首先安装gtk2.0-dev与pkg-config以进行视频通话(cv.destroyallwindows的报错)

   解决opencv与pyside的plugin冲突导致的报错

   ```
   pip install opencv-python-headless
   ```

   

5. 请参考`requirements.txt`完成余下的配置

# 啰嗦两句

受限于当时的水平与时间，我对于代码结构是不太满意的：有更多代码可以复用，在封装上也可以做得更加优雅。越往后，越为了实现功能而不断向屎山靠拢。起初我们是对标着微信来设计的，不过受限于实力和时间，对一些功能做了阉割。请务必注意有一些地方我们的代码处理还不够完善（比如文件收发：当文件没有发送完毕，接收会bug），希望后来者能够补足。初此之外，有几个重要的缺陷是我必须交代的：

1. 并行的线程管理：几乎没有去管这方面，属于是摆了
2. socket管理：几乎没有去管这方面，属于是摆了
3. 数据安全性：几乎没有去管这方面，属于是摆了
4. whisper在不同设备上表现差异较大，没理解

还有一些琐碎的问题，包括但不限于

1. 发送&接收的文件重名处理
2. 有反映用户id难记，想换个方式登录的
3. 人脸识别效果很差，没实装
4. 发送的如果是图片，直接显示为图片而不是文件
5. 头像动态刷新（现在是退出登录之后才会刷新）
6. 语音识别目前是固定录制5秒，没来得及做自由控制时间的
7. 我觉得UI做的不够好看，~~虽然Qt负责者TT2TER很满意~~
8. 消息框滚动位置的小细节
9. 其它问题



by PM [@FluppyFR](https://github.com/fpyyy) 2023.9.6