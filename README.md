# HITqa&YXRobot
目录总览：
![](https://github.com/AIRobotZhang/HITqa-YXRobot/raw/master/pic1.png)  

这是webflask应用V2.0版本，目前实现的功能有：注册、登录、发布问答、查询、评论以及基于aiml的在线聊天、上传aiml文件新功能
新功能web页面展示（原功能页面可到webflask应用V1.0版本查看https://github.com/AIRobotZhang/WebFlask）：
![](https://github.com/AIRobotZhang/HITqa-YXRobot/raw/master/pic2.png)  

1.运行该项目之前，相应包以及一些扩展的安装，webflask应用V1.0版本（https://github.com/AIRobotZhang/WebFlask）都有介绍，在此不再赘述，需要引进的新包为aiml以及werkzeug

2.需要说明的是webflask应用V1.0版本中我们的首选方式就是创建一个虚拟环境 ,这个环境能够安装所有的东西，而此时我们的主Python不会受到影响。但是虚拟环境的迁移性不是很好，在webflask应用V2.0版本中，我考虑使用docker封装镜像的方法来进行web应用的封装，这样做的优点是迁移性较好，具体参考网址如下：http://www.runoob.com/docker/docker-tutorial.html、http://www.cnblogs.com/xiadongqing/p/6144265.html

3.在我们的项目中需要涉及数据库的连接，那么在运行项目之前就需要修改config.py里的配置，包括HOSTNAME（本机ip）、DATABASE（数据库名称）、USERNAME（MySQL登录用户名）、PASSWORD（MySQL登录密码），具体如下图：
![](https://github.com/AIRobotZhang/HITqa-YXRobot/raw/master/pic3.png) 

4.在models.py文件中是数据模型，当增添新的数据模型时，需要将其重新映射到数据库中，所以在运行该项目之前需要进行映射，步骤如下：
  如果采用虚拟环境的方式，首先进入虚拟环境的命令环境下，其次，进入到manage.py项目文件目录下，依次在命令行窗口下执行如下两条命令：python manage.py db migrate 和 python manage.py db upgrade ,映射成功，可到数据库命令行窗口查看
  如果采用docker，需要在Dockerfile文件中写明，具体可查看该文件，其中requirements.txt包含了该项目需要安装的包
  
5.另外，注册密码进行MD5加盐加密后存入数据库中

6.在进行对话时，需要确认自己的aiml文件的存放位置，以及上传文件的存储位置，否则容易出错，具体如下图：
![](https://github.com/AIRobotZhang/HITqa-YXRobot/raw/master/pic4.png) 
![](https://github.com/AIRobotZhang/HITqa-YXRobot/raw/master/pic5.png) 

7.运行hitqa.py文件可运行该项目
 
 
