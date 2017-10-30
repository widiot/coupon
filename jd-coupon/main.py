import requests
import datetime

# 抢券的时间
scheduled_time = "2017-10-30 00:00"
# 券的URL
couponUrl = "https://act-jshop.jd.com/couponSend.html?callback=jQuery7718692&roleId=8620903&key=10e5977effdf438a8f61cb95b576e0f5&_=1509292645477"
# 券的Referer
referer = "https://sale.jd.com/act/hznk5FbYfOTiEp.html"
# 浏览器及版本
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'


# 将cookie转为字典
def get_cookie():
    with open("cookie.txt") as f:
        cookies = {}
        for line in f.read().split(';'):
            name, value = line.strip().split('=', 1)
            cookies[name] = value
        return cookies


# 配置Session的参数
session = requests.Session()
session.headers['User-Agent'] = user_agent
session.headers['Referer'] = referer
session.cookies = requests.utils.cookiejar_from_dict(get_cookie())


# 开始抢券
def getCoupon():
    print('等待抢券中......')
    while (True):
        # 当前时间
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')

        # 如果到预定时间就开始发送请求，然后打印结果
        if now == scheduled_time:
            r = session.get(couponUrl)
            print(r.text)
            break


if __name__ == '__main__':
    getCoupon()
