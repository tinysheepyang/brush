web刷量 python+selenium+xvfb+Firefox打开浏览器浏览网页<br />
python2.7 selenium==2.53.6<br />

1.centos xvfb安装<br />
yum install firefox -y
yum install -y Xvfb
yum -y install libXfont
yum install xorg-x11-fonts*
将config目录下xvfb文件copy到/etc/init.d/目录下
chmod +x /etc/init.d/xvfb
chkconfig xvfb on
service xvfb start
在/etc/profile文件尾部追加一行export DISPLAY=:7

2.依赖<br />
requests
redis
xvfbwrapper
xlwt
fake_useragent
firefox

3.创建数据库<br />
mysql连接为mysql -uroot -pyimaoxxx -hdb.lan brush
请设置相应的用户名密码并创建brush库，db.lan为/etc/hosts文件对应的ip地址
创建完brush库将config下brush.sql 导入brush库 mysql -uroot -pyimaoxxx -hdb.lan bursh < brush.sql

4.创建redis<br />
redis主要是存储ip资源，ip资源通过快代理获取需要付费http://dps.kuaidaili.com/api/getdps/?orderid=996639436139576&num=30&ut=1&format=json&sep=2
redis 默认端口为6379 redis.lan 为/etc/hosts 文件所对应ip，key为proxy_list，程序运行第一重要的事就是从proxy_list获取ip 如果没有ip程序将运行失败
从代理获取ip存储到redis脚本为config目录下

5.使用python fake_useragent库<br />
fake_useragent需要在线生成被墙了
将config目录下fake_useragent_0.1.2.json文件拷贝到tmp目录下

6.运行<br />
运行run.py文件即可启动程序，增加刷量词请修改对应Page目录下conf.py、page\homepage.py、testcase\validations.py

7.发送刷量结果<br />
每个词的搜索次数点击次数都存储在redis 1库和2库，每天凌晨从redis获取到刷量结果生成html文件发送给相关责任人
生成html脚本为config下html.py 发送邮件脚本为mail.py
