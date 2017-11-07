import requests
import datetime

# 抢券的时间
scheduled_time = "2017-11-07 22:00"
# 券的URL
requestUrls = ["https://act-jshop.jd.com/couponSend.html?callback=jQuery8299904&roleId=8875111&key=a9185b7963d74999bdfde0ab214b31bb&_=1510062919603","https://act-jshop.jd.com/couponSend.html?callback=jQuery9197213&roleId=8817197&key=7b9cef8b76f64c3ba2474e810382d69b&_=1510062967022"]
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
        if now >= scheduled_time:
            for i in range(len(requestUrls)):
                session.headers['Referer'] = referers[i]
                r = session.get(requestUrls[i])
                print(r.text)
            break


if __name__ == '__main__':
    getCoupon()
