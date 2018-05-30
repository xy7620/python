import urllib,re
from urllib import request
from http import cookiejar
from auto_login.log import logger

def login(url, id, passw, action='login'):
    logging = logger
    # 封装头信息，伪装成浏览器
    header = {
    'Connection': 'Keep-Alive',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0(compatible;MSIE9.0;WindowsPhoneOS7.5;Trident/5.0;IEMobile/9.0;HTC;Titan)',
    'X-Requested-With': 'XMLHttpRequest'
    }

    login_data = urllib.parse.urlencode({
        'action': action,
        'username': id,
        'pass': passw
    }).encode(encoding='utf8')

    try:
        req = request.Request(url, login_data, headers=header)
        cj = cookiejar.LWPCookieJar()
        opener = request.build_opener(request.HTTPCookieProcessor(cj))
        # request.install_opener(opener)

        resp = opener.open(req)
        page = resp.read().decode('utf8')
        # print(page)
        pattern = '本次登录获得 \d* 积分|积分:\d*'
        result = re.search(pattern, page)
        if result:
            points = result.group()
            # print(points)
            return points
        else:
            if page.find('用户名或密码错误，请注意区分大小写') > -1:
                s = '用户'+id+' 用户名或密码错误，请注意区分大小写'
                logging.warning(s)
                print(s)
                return -1
            s = '用户'+id+'未找到积分，可以登录'
            logging.error(s+'\n')
            return -1

    except Exception as e:
        print('用户',id, url,' 登录失败！')
        print(e)
        return -1


if __name__ == '__main__':
    url = 'www.baidu.com'
    id = '762031227108'
    passw = '1231401230'
    action = 'login'
    login(url, id, passw, action)

