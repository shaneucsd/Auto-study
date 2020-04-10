# Auto-study
通过Selenium实现腾讯课堂定时自动进入课堂
详见 Auto_study.ipynb
## Table of Contents
* ![Introduction](#Introduction)
* ![Setup](#Setup)
* ![Using](#Using)
## 1.Introduction
腾讯课堂的自动进入课堂程序，保证学生在课前5分钟自动打开课堂界面，强制进入学习。
## 2.Setup
1. 查询目前chrome应用程序的版本并下载[chromedriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)，需下载与本地chrome对应的chromedriver版本<br>

2. 下载selenium 
    ```pip install selenium -i https://pypi.tuna.tsinghua.edu.cn```
    
3. 替代chromedriver 路径
    <br>进入auto_dont_study.py的get_driver
    <br>用chromedriver的路径替换 driver = webdriver.Chrome('chromedriver的路径')
    
# 3.Using
### 3.1首次登陆，保存cookies到本地
```
from auto_study import auto_study 
study = auto_study()
study.login(first_time=True)
study.quit()
```
### 3.2自动进入最近一节课的直播
运行direct_study函数
```
study.direct_study()
```
### 3.3自动开始一节课的学习

TODO:需要修改课程切换的bug，在同一个页面不能切换到指定课程的界面
<br>
1.新建该目录下新建一个python文件,如 essay_study.py
    2.在腾讯课堂中记录课程名字(腾讯课堂显示的名字），传入coursename参数
    3.将课程时间（分钟）传入course_time_by_minute参数
    4.每次开始学习一节课就按上述方法创建一个python文件(供定时开始上课）
   
```
#essay_study内容
study.study(course_name='经贸研究与论文写作-2-谢红军',course_time_by_minute=90)
```
    
### 3.4定时开始一节课

你须是**mac/linux**系统才能用这个命令
#### 3.4.1制作定时命令
1. 制作定时命令的时间部分 格式如下
     分钟 小时 * * 周几 
     <br>e.g:
     如果要在周一的8点59分进入课堂,命令如下：
     ```59 8 * * 1```
     
2. 制作定时命令的python部分
    * 打开Terminal，输入 ```which python```
    <br>复制输出结果
    e.g:
    ```/usr/bin/python```
3. 制作定时命令的python文件部分
    * 打开Terminal，将要运行的课程文件拖入terminal<br>复制输出结果
    e.g:
    ```/usr/Ciwei/essay_study.py```
4. 将三部分命令拼在一起，就是定时命令
    <br>e.g:
    ```59 8 * * 1 /usr/bin/python /usr/Ciwei/essay_study.py```
    
#### 3.4.2在crontab中配置这个定时命令

* 在Terminal中输入
```crontab -e```
* 按i键进入vim编辑, 将上述命令粘贴至新的一行
* 按Esc键退出编辑，依次按下wqZZ保存并退出crontab


### 完成！ 开始愉快地学习吧！
自动上课虽然很爽，但是一定要认真听课噢！
