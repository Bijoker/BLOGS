# 解决chrome安装谷歌访问助手错误问题

针对新版本安装谷歌访问助手插件报错问题

1、下载谷歌访问助手

<http://www.ggfwzs.com/>

2、chrome浏览器打开发者模式

3、将下载的crx 文件拖入拓展程序，发现加载程序错误！！！

# 重点

1、首先将crx文件后缀改为zip，例如：

```
谷歌访问助手2.2.2.crx  改为 谷歌访问助手2.2.2.zip
```

2、将该文件解压，会解压出包含几个文件的文件夹

![](https://img2018.cnblogs.com/blog/1600965/201904/1600965-20190422100959489-721923305.png)


3、chrome 拓展程序中选择加载**已解压程序包**  ,选择刚才的文件

4、如果改变后缀名名后文件解压失败， 可尝试rar或者其他压缩类型重新以上步骤！