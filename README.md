# 参数获取

---

要实现发送请求抢券，需要获取券的`URL`，并定制请求头`Request Headers`

下面所有参数都来自Chrome的开发者工具。大多浏览器都有开发者工具，可以按需选择

准备步骤：

1. 登录网站
2. 进入抢券页面
3. 打开开发者工具（Chrome的快捷键是F12）
4. 切换到Network栏
5. 按F5刷新抢券页面

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

# 脚本实现

---

目录结构

```
coupon/
    __init__.py
    cookie.txt
    main.py
```

1. 将复制的`cookie`复制到`cookie.txt`文件中

    ```
    ipLoc-djd=1-72-2799-0; ipLocation=%u5317%u4EAC; areaId=1; ......
    ```

2. 写一个把`cookie.txt`转为字典的函数

    ```
    def get_cookie():
    with open("cookie.txt") as f:
        cookies={}
        for line in f.read().split(';'):
            name,value=line.strip().split('=',1)
            cookies[name]=value
        return cookies
    ```

2. 配置参数

    ```
    user_agent = 'Mozilla/5.0 ......'
    couponUrl = 'https://act-jshop.jd.com/couponSend.html? ......'
    referer = 'https://sale.jd.com/act/hznk5FbYfOTiEp.html'
    ```

4. 声明一个Session对象，并将参数赋值给他

    ```
    session = requests.Session()
    session.headers['User-Agent'] = user_agent
    session.headers['Referer'] = referer
    session.cookies = requests.utils.cookiejar_from_dict(get_cookie())
    ```

5. 设置一个`while(True)`的循环，将预定时间和当前时间比较，如果相等，就发送请求

    ```
    while (True):
        # 当前时间
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')

        # 如果到预定时间就开始发送请求，然后打印结果
        if now == scheduled_time:
            r = session.get(couponUrl)
            print(r.text)
            break
    ```
