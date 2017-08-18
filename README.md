# 百度贴吧一键签到

基于Python3.6 于2017年8月8日16:19:35在centos7上测试成功

百度贴吧零点一键签到系统，此程序需要百度的cookies，直接在本地的当前文件创建一个cookies.txt文件，把cookies放进去即可。百度第一个cookies需要将: g改为; 具体看cookies

具体如何获得cookies百度。（document.cookie 获取的cookies一直报错，具体原因不详。我自己是抓包，抓到cookies的）


# 测试

在昨天测试成功了。放在我的阿里云服务器上了，在凌晨执行成功了。

具体代码如下：

1: at 04:30 

2: ./TiebaSign.py 

3: ctrl+d 

测试结果如下：

![Image text](https://github.com/wenbochang888/TiebaSign/blob/master/img/1.png)

![Image text](https://github.com/wenbochang888/TiebaSign/blob/master/img/2.png)

# crontab命令

使用crontab命令直接放服务器，让他每天在零点执行脚本

1:  crontab -e

2： 0  0  *  *  *  /home/chang/TiebaSignpp.py >> /home/chang/tieba.log 2>&1

3： 保存退出

于2017年8月8日16:28:02测试成功

![Image text](https://github.com/wenbochang888/TiebaSign/blob/master/img/3.png)
  

# 欢迎fork，star 

每天抢首签，做15级大水逼不是梦想