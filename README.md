# 协同飞行任务 
    python3.9


## 1、安装方式
    下载：Code——Download ZIP    或   GIT:https://github.com/lixiaohuahuahua/Collaborative-flight.git

### <center>    安装配置库：`pip install -r requirements.txt`

## 2、检查操纵杆编号和按钮编号
### <center>`python buttoncheck.py`
    检查两个操纵杆的编号（number of joystick）和每个操纵杆对应的按钮的编号（button number）
    确定扳机的按钮编号

## 3、协同打击任务
### 鼠标和空格版本：
### <center>`python main.py`
### 当确定好了编号，需要修改参数（注释中已经标好）
### <center>[joystick_xietong.py](joystick_xietong.py)
### <center>`python joystick_xietong.py`


![hit.PNG](picture%2Fhit.PNG)

### 操作方法：
            用户A使用操纵杆1进行瞄准

            用户B使用操纵杆2的扳机进行射击



## 4、躲避&搜索任务
### <center>`python search.py`

### 操作方法：
            用户A使用↑↓/←→方向键 or 操纵杆 控制飞机躲避
            (获取操纵杆位置的代码注释掉了，看需要什么)

            用户B使用鼠标进行视觉搜索任务（逻辑待完善）
