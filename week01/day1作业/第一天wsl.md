1.什么是wsl？
一种运行在widows系统上的Linux子系统

2.为什么要用wsl？
AI agent在Linux系统上表现较好，且代码最终大概率要部署到Linux的服务器上，同时也能和Windows系统进行隔离，防止出错影响到Windows系统。

3.什么是ubuntu？
最流行的Linux操作系统，类似安卓手机中的不同厂商的操作系统，底层都是安卓，ubuntu的底层就是Linux。

4.相关命令
wsl ---启动
wsl -d xxx 启动特定的虚拟机
exit 退出
wsl --set-default xxx设置默认分发
sudo xx以超级用户身份运行
pwd -- 查看当前路径
ls  --查看当前目录所有文件
cp  --复制文件
cd  --移动到
rm  --删除
mkdir --创建文件夹
find --查找
ifconfig --查看命令
su xx --登陆用户xx
shutdown --关闭虚拟机，退出用exit
vi --编写文件
touch --创建文件
scp --发送文件
unzip --解压
chmod +x xx.txt --执行权限
realpath --显示绝对路径
file --识别文件类型
