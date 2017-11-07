import requests
import datetime

# 抢券的时间
scheduled_time = "2017-11-07 20:11"
# 券的URL
requestUrls = ["https://act-jshop.jd.com/couponSend.html?callback=jQuery2891171&roleId=8781460&key=48b40c64619a4bc9a3912c98d5a94fed&_=1510055639531","https://act-jshop.jd.com/couponSend.html?callback=jQuery6218594&roleId=8725660&key=a606cfe7c5b045d1b5e58b43a59fd9b1&_=1510056463018"]
# 券的Referer
referers = ["https://sale.jd.com/act/bD1USlOE8n.html","https://sale.jd.com/act/bD1USlOE8n.html"]
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
session.cookies = requests.utils.cookiejar_from_dict(get_cookie())


# 开始抢券
def getCoupon():
    print('等待抢券中......')
    while (True):
        # 当前时间
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')

        # 如果到预定时间就开始发送请求，然后打印结果
        if now == scheduled_time:
            for i in range(len(requestUrls)):
                session.headers['Referer'] = referers[i]
                r = session.get(requestUrls[i])
                print(r.text)
        break


if __name__ == '__main__':
    getCoupon()
