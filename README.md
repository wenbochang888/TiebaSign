# 百度贴吧一键签到

基于Python3.6 于2017年8月8日16:19:35在centos7上测试成功

百度贴吧零点一键签到系统，此程序需要百度的cookies，直接放在本地下面就可以

具体如何获得cookies百度。（百度的加密看的不太懂，直接cookies方便）


# 测试

在昨天测试成功了。放在我的阿里云服务器上了，在凌晨执行成功了。

具体代码如下：

1: at 04:30 2: ./TiebaSign.py 3: ctrl+d 

测试结果如下：

![Image text](https://github.com/wenbochang888/gdufeInformation/blob/master/0.png)

# crontab命令

使用crontab命令直接放服务器，让他每天在零点执行脚本

1:  crontab -e  
2： 0 0 * * * /home/chang/TiebaSign.py
3： 保存退出

于2017年8月8日16:28:02测试成功

![Image text](https://github.com/wenbochang888/gdufeInformation/blob/master/0.png)
  

# 欢迎fork，star 

每天抢首签，做15级大水逼不是梦想