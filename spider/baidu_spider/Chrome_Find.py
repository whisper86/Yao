# 作者：许垚
# 开发时间2022年10月19日

import webbrowser


def Find():
    quary = "hello"
    # 浏览器运行目录
    chromePath = "../Yao/Applications/Google\ Chrome.app"

    # 注册浏览器
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chromePath))

    # 获取浏览器并打开指定地址
    webbrowser.get('chrome').open(
        f"https://www.so.com/s?ie=utf-8&src=hao_360so_b_cube&shb=1&hsid=a2ae26d14370ef37&ssid=&q={quary}", new=1,
        autoraise=True)


Find()
