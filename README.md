>博客地址——[Python脚本实现抢券](http://blog.csdn.net/white_idiot/article/details/78385441)

# 参数获取

要实现发送请求抢券，需要获取券的`URL`，并定制请求头`Request Headers`

下面所有参数都来自Chrome的开发者工具。大多浏览器都有开发者工具，可以按需选择

准备步骤：

1. 登录网站
2. 进入抢券页面
3. 打开开发者工具（Chrome的快捷键是F12）
4. 切换到Network栏

![](http://upload-images.jianshu.io/upload_images/2482101-0cb61f096e57f9cf.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

## 获取券的URL

在上面准备步骤的基础上，点击想要抢的券，这时`Name`栏底部会出现一个新的链接，点击这个链接，而我们需要的参数就来自`Header`中

复制`Request URL`

```
https://act-jshop.jd.com/couponSend.html? ......
```

![](http://upload-images.jianshu.io/upload_images/2482101-0568fcfc9128cd54.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

## 获取Cookie

也是在上面这个页面中，下翻在`Request Header`中，有一个`Cookie`的参数，复制下来

```
ipLoc-djd=1-72-2799-0; ipLocation=%u5317%u4EAC; areaId=1; ......
```

![](http://upload-images.jianshu.io/upload_images/2482101-f65ea39c17d73c2a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

## 获取券的Referer

同上，复制`Referer`参数

```
https://sale.jd.com/act/hznk5FbYfOTiEp.html
```

# 运行

直接在命令行运行

```
python main.py
```

![](http://upload-images.jianshu.io/upload_images/2482101-16e1c54f95521402.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

看见上面这几个字气不气？？？

# 后记

终于抢到券了，但是。。。

最后一天突然券的数量变多了，完全不用抢

这。。。骗子！

![](http://upload-images.jianshu.io/upload_images/2482101-ab1d7c9baf852edc.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

不过看到这行字还是挺开心的

有些时候要同时抢几张券，所以把参数改成了列表

```
# 券的URL
requestUrls = ["https://act-jshop.jd.com/couponSend.html?callback=jQuery2891171&roleId=8781460&key=48b40c64619a4bc9a3912c98d5a94fed&_=1510055639531","https://act-jshop.jd.com/couponSend.html?callback=jQuery6218594&roleId=8725660&key=a606cfe7c5b045d1b5e58b43a59fd9b1&_=1510056463018"]

# 券的Referer
referers = ["https://sale.jd.com/act/bD1USlOE8n.html","https://sale.jd.com/act/bD1USlOE8n.html"]

# 如果到预定时间就开始发送请求，然后打印结果
        if now == scheduled_time:
            for i in range(len(requestUrls)):
                session.headers['Referer'] = referers[i]
                r = session.get(requestUrls[i])
                print(r.text)
            break
```

![](http://upload-images.jianshu.io/upload_images/2482101-3332eb610d1baf4e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

